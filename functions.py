import json
import os
from config import user_input_test, ALLOWED_CATEGORIES, PRIMARY_MODEL_PROVIDER,SECONDARY_MODEL_PROVIDER, MODEL_MAP, VERSION
import time
from model import HFClient, GEMINIClient
from validation import validate_test_cases
import logging
from persistence import save_results, save_session, retrieve_session
from evaluation import evaluation
from cleaner import clean_response
import torch
from transformers import pipeline


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

      failed_tests=[]
      passed_tests=[]
      test_results=[]
      session={}
      category_results = {}
      ERROR_COUNTS = {
      "MODEL_ERROR": 0,
      "CLEANER_ERROR": 0,
      "PARSE_ERROR": 0,
      "VALIDATION_ERROR": 0
      }

      validate_test_cases(user_input_test, ALLOWED_CATEGORIES)

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

      return failed_tests, passed_tests, test_results,session, category_results,ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode

def run_test_case(client, prompt, validation_function):
      
      start_time=time.time()
      max_retriess=3
      retries =1
      parsed_data=None
      validation_errors=[]
      error_type=None
      test_status="failed"

      while retries < max_retriess:
                        
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

      return test_status, parsed_data, duration, error_type, retries, validation_errors

def process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, retries, error_type,validation_errors, duration,parsed_data, provider):
      
      logger.info(f"{test_name} - {test_status}")

      cat = test_case["category"]
      if cat not in category_results:
            category_results[cat] = {"passed": 0, "failed": 0}

      if test_status == "passed":
            category_results[cat]["passed"] += 1
            passed_tests.append(test_name)
      else:
            category_results[cat]["failed"] += 1
            failed_tests.append(test_name)

      test_results.append({"name":test_name,"status":test_status,"retriess":retries,"error_type":error_type,"errors":validation_errors,"duration":duration,"provider":provider})
      session.update({"name":test_name,"mode":mode,"provider":provider,"input":user_input, "output":parsed_data})
      logger.info(f"{test_name} is finished.")

def finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session,total_tries, total_duration):
      
      test_summary={}

      for err, count in ERROR_COUNTS.items():
            logger.info(f"{err}: {count}")

      for cat, stats in category_results.items():
            logger.info(f"Category {cat}: {stats['passed']} passed, {stats['failed']} failed")
            total_failed_tests=len(failed_tests)
            total_passed_tests=len(passed_tests)
            total_tests=total_passed_tests+total_failed_tests
            overall_success_rate=total_passed_tests/total_tests
            avg_duration=total_duration/total_tests
            avg_tries=total_tries/total_tests
            category_success_rate=stats["passed"]/total_tests
            category_results[cat]["succes_rate"]=category_success_rate

      test_summary.update({"overal_succes_rate":overall_success_rate,"category_success_rate":category_success_rate,"avg_duration":avg_duration,"avg_tries":avg_tries,"version":VERSION})
      logger.info(f"Aggregated run metrics: Overall success rate - {overall_success_rate}, Category success rate - {category_success_rate}, Average duration: {avg_duration:.2f}s, Average retries - {avg_tries}, Version - {VERSION}")

      
      

      evaluation(failed_tests, passed_tests)
      save_results(test_results, mode, test_summary)
      save_session(session)


def prepare_test_case(test_name,user_input, input_based_on_mode):
            
            logger.info(f"Test {test_name} started.")

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
        logger.error(f"Converting speach to text filed: {e}")
        raise