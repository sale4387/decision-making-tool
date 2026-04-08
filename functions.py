import json
import os
from config import user_input_test, ALLOWED_CATEGORIES, PRIMARY_MODEL_PROVIDER,SECONDARY_MODEL_PROVIDER, MODEL_MAP
import time
from model import HFClient, GEMINIClient
from validation import validate_test_cases
import logging
from persistence import save_results, save_session, retrieve_session
from evaluation import evaluation
from cleaner import clean_response


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
      session=[]
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
      max_attempts=3
      attempt =0
      parsed_data=None
      validation_errors=[]
      error_type=None
      test_status="failed"

      while attempt < max_attempts:
                        
                        try:
                              raw_response = client.api_call(prompt)
                        except Exception:
                              attempt += 1
                              logger.debug(f"Attempt {attempt} failed, model error.")
                              error_type = "MODEL_ERROR"
                              continue

                        cleaner_status, json_text= clean_response(raw_response)
                        
                        if cleaner_status == False:
                              attempt+=1
                              logger.debug(f"Attempt {attempt} failed, no JSON object found.")
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
                                    attempt+=1
                                    logger.debug(f"Attempt {attempt} failed, validation error(s).")
                                    error_type="VALIDATION_ERROR"
                                    continue
                        except json.JSONDecodeError:
                                attempt+=1
                                logger.debug(f"Attempt {attempt} failed, parsing error.")
                                error_type="PARSE_ERROR"
                                continue
                        
      end_time=time.time()
      duration=end_time-start_time

      return test_status, parsed_data, duration, error_type, attempt, validation_errors

def process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, attempt, error_type,validation_errors, duration,parsed_data, provider):
      
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

      test_results.append({"name":test_name,"status":test_status,"attempts":attempt,"error_type":error_type,"errors":validation_errors,"duration":duration,"provider":provider})
      session.append({"name":test_name,"mode":mode,"provider":provider,"input":user_input, "output":parsed_data})
      logger.info(f"{test_name} is finished.")

def finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session):
      
      for err, count in ERROR_COUNTS.items():
            logger.info(f"{err}: {count}")

      for cat, stats in category_results.items():
            logger.info(f"Category {cat}: {stats['passed']} passed, {stats['failed']} failed")

      evaluation(failed_tests, passed_tests)
      save_results(test_results, mode)
      save_session(session)
      session_history=retrieve_session()

      logger.info("Last 5 lines:")
      for line in session_history:
            logger.info(f"Id: {line['id']} - Timestamp:{line['timestamp']}\n")

def prepare_test_case(test_case, input_based_on_mode):
            test_name= test_case["name"]
            logger.info(f"Test {test_case['name']} started.")
            user_input=test_case["input"]
            prompt=input_based_on_mode.replace("{user_input}", user_input)

            return test_name, user_input, prompt