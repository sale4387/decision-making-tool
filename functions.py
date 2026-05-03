import json
import os
from config import PRIMARY_MODEL_PROVIDER,SECONDARY_MODEL_PROVIDER, MODEL_MAP, VERSION
import time
from model import HFClient, GEMINIClient
import logging
from persistence import save_results, save_session, retrieve_session
from cleaner import clean_response
import torch
from transformers import pipeline
import difflib


logger=logging.getLogger(__name__)

PROVIDER_MAP={
      "huggingface":HFClient,
      "google":GEMINIClient
}

def get_mode_input(mode):
      BASE_DIR = os.path.dirname(__file__) 
      template_path = os.path.join(BASE_DIR, "templates", f"{mode}.txt")
      with open (template_path, "r") as file:
            file_content=file.read()
      return file_content

def init_test_case(mode):

      test_results=[]
      session={}
 

      primary_model_name=MODEL_MAP[PRIMARY_MODEL_PROVIDER]
      primary_client_class = PROVIDER_MAP.get(PRIMARY_MODEL_PROVIDER)
      secondary_model_name=MODEL_MAP[SECONDARY_MODEL_PROVIDER]
      secondary_client_class = PROVIDER_MAP.get(SECONDARY_MODEL_PROVIDER)

      if primary_client_class is None or secondary_client_class is None:
            logger.error(f"Wrong provider selected")
            exit(1)
      primary_client= primary_client_class(primary_model_name)
      secondary_client= secondary_client_class(secondary_model_name)

      
      input_based_on_mode =get_mode_input(mode)

      return test_results,session,primary_client, secondary_client, input_based_on_mode

def run_test_case(client, prompt, validation_function, user_input):
      
      start_time=time.time()
      max_retriess=3
      retries =1
      parsed_data=None
      validation_errors=[]
      error_type="None"
      test_status="failed"
      max_model_callss=7
      model_calls=0
      test_score=None

      while retries < max_retriess:
                        
                        if model_calls >= max_model_callss:
                              logger.debug(f"Max model calls reached: {model_calls}")    
                              raise Exception(f"Max model calls reached: {model_calls}")
                        model_calls+=1

                        try:
                                    raw_response = client.api_call(prompt)
                        except Exception:
                                    retries += 1
                                    logger.debug(f"Try {retries} failed, model error.")
                                    error_type = "MODEL_ERROR"
                                    continue



                        cleaner_status, json_text= clean_response(raw_response)
                        
                        if cleaner_status == False:
                              retries+=1
                              logger.debug(f"Try {retries} failed, no JSON object found.")
                              error_type="CLEANER_ERROR"
                              continue
                        try:
                              parsed_data=json.loads(json_text)
                              validation_passed, validation_errors= validation_function(parsed_data)
                              if validation_passed:
                                    test_status="passed"
                                    test_score=get_score(parsed_data,user_input)
                                    error_type=None
                                    break
                              else:
                                    retries+=1
                                    logger.debug(f"Try {retries} failed, validation error(s).")
                                    error_type="VALIDATION_ERROR"
                                    continue
                        except json.JSONDecodeError:
                                retries+=1
                                logger.debug(f"Try {retries} failed, parsing error.")
                                error_type="PARSE_ERROR"
                                continue
                        
      end_time=time.time()
      duration=end_time-start_time
      duration=f"{duration:.2f}"

      return test_status, parsed_data, duration, error_type, retries, validation_errors, model_calls,test_score

def process_test_results(test_status,test_results,session,mode, user_input, retries, error_type,validation_errors, duration,parsed_data, provider, model_calls, fallback, test_score):
      

      logger.info(f"Test - {test_status}")
      test_results.append({"status":test_status,"retries":retries,"error_type":error_type,"errors":validation_errors,"duration":duration,"quality":test_score,"provider":provider,"calls":model_calls,"fallback":fallback})
      session.update({"mode":mode,"provider":provider,"input":user_input, "output":parsed_data})
      logger.info(f" Test is finished.")

def finalize_test_run(mode,test_results,session):
      

      save_results(test_results, mode)
      save_session(session)


def prepare_test_case(user_input, input_based_on_mode, mode):
            
            logger.info(f"Test started. Mode: {mode}")

            session_history=retrieve_session()

            previous_inputs = []
            previous_outputs = []

            for session in session_history:
                  previous_inputs.append(session.get("results", {}).get("input", ""))
                  previous_outputs.append(session.get("results", {}).get("output", ""))
            previous_inputs_text = "Previous inputs:\n" + "\n".join(previous_inputs)            
            previous_outputs_text = "\n".join([json.dumps(o) for o in previous_outputs])

            prompt=input_based_on_mode.replace("{user_input}", user_input).replace("{previous_inputs}",previous_inputs_text).replace("{previous_responses}", previous_outputs_text)
            return prompt

def convert_voice_to_text(audio_file):
    try:
        speech_to_text = pipeline(
            task="automatic-speech-recognition",
            model="openai/whisper-tiny",
            device=-1
        )
        converted_text= speech_to_text(audio_file)["text"]
        return converted_text
    except Exception as e:
        logger.error(f"Converting speech to text filed: {e}")
        raise
    
def get_score(parsed_data, user_input):
    goal = parsed_data.get("goal", "")
    seq = difflib.SequenceMatcher(None, user_input.lower(), goal.lower())
    goal_score = seq.ratio()

    total_pros = sum(len(parsed_data["pros_cons"][opt]["pros"]) for opt in parsed_data["options"])
    total_cons = sum(len(parsed_data["pros_cons"][opt]["cons"]) for opt in parsed_data["options"])

    if (total_pros + total_cons) == 0:
        pros_score = 0
    else:
        pros_score = total_pros / (total_pros + total_cons)

    final_score = (goal_score + pros_score) / 2

    if final_score > 0.7:
        return "great"
    elif final_score >= 0.4:
        return "good"
    else:
        return "bad"


