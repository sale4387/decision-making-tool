import argparse
from model import call_model
from config import user_input_test, model_instructions, allowed_log_levels
import time
from model import call_model
import json
from validation import validate_response_default, validate_response_partial, validate_response_minimal
from model import call_model
from evaluation import evaluation
from cleaner import clean_response
from persistence import save_results
import logging, logger

logger=logging.getLogger(__name__)

failed_tests=[]
passed_tests=[]
test_results=[]

def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode")
    parser.add_argument("-l", "--llevel")
    args = parser.parse_args()
    return args.mode, args.llevel.upper() if args.llevel else None

def function_test(mode):
      for test_case in user_input_test:
            logger.info(f"Test {test_case['name']} started.")
            user_input=test_case["input"]
            prompt=f"""{model_instructions["default"]} Now here is the input: {user_input}"""
            max_attempts = 3
            attempt = 0
            start_time=time.time()

            while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)
                        cleaner_status, json_text= clean_response(raw_response)
                        if cleaner_status == False:
                              attempt+=1
                              logger.debug(f"Attempt {attempt} failed, no JSON object found.")

                              continue
                        try:
                                parsed_data=json.loads(json_text)
                                response_validated= validate_response_minimal(parsed_data)

                                if response_validated[0]:
                                    passed_tests.append(test_case['name'])
                                    test_status="passed"
                                    break
                                else:
                                    attempt+=1
                                    logger.debug(f"Attempt {attempt} failed, validation error(s).")

                                    continue
                                
                        except json.JSONDecodeError as e:
                                attempt+=1
                                logger.debug(f"Attempt {attempt} failed, pharsing error.")

                                continue
                        
            end_time=time.time()
            duration=end_time-start_time
                
            if attempt == max_attempts:   
                    failed_tests.append(test_case['name'])
                    test_status="failed"

            logger.info(f"{test_case['name']} - {test_status}")
            test_results.append({"name":test_case['name'],"status":test_status,"attempts":attempt,"errors":response_validated[1],"duration":duration})
            logger.info(f"{test_case['name']} is finished.")

      evaluation(failed_tests, passed_tests)
      save_results(test_results, mode)

def function_plan(mode):
      for test_case in user_input_test:
            logger.info(f"Test {test_case['name']} started.")
            user_input = test_case["input"]
            prompt= f"{model_instructions["plan"]} Now here is the input: {user_input}"
            max_attempts = 3
            attempt = 0
            print(f"\n ====== Running test: ======\n {test_case['name']}\n")
            start_time=time.time()

            while attempt < max_attempts:
                  raw_response=call_model(prompt)

                  cleaner_status, json_text= clean_response(raw_response)

                  if cleaner_status == False:
                        attempt+=1
                        print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt} failed.\n')
                        logger.debug(f"Attempt {attempt} failed, no JSON object found.")
                        continue

                  try:
                      parsed_data=json.loads(json_text)
                      response_validated = validate_response_partial(parsed_data)

                      if response_validated[0]:
                            print("====== GOAL ======")
                            print(parsed_data.get("goal"), "\n" )
                            print("====== OPTIONS ======\n")
                            print(parsed_data.get("options"), "\n")
                            print("====== NEXT STEPS ======\n")
                            print(parsed_data.get("next_steps"), "\n")
                            passed_tests.append(test_case['name'])
                            test_status="passed"
                            break
                      
                      else:
                        attempt+=1
                        logger.debug(f"Attempt {attempt} failed, validation error(s).")

                        continue
                      
                  except json.JSONDecodeError as e:
                        attempt+=1
                        logger.debug(f"Attempt {attempt} failed, pharsing error.")

                        continue

            end_time=time.time()
            duration=end_time-start_time #measuring time needed for model to respond
            
            if attempt == max_attempts:

                  failed_tests.append(test_case['name'])
                  test_status="failed"
                  
            logger.info(f"{test_case['name']} - {test_status}")
            test_results.append({"name":test_case['name'],"status":test_status,"attempts":attempt,"errors":response_validated[1],"duration":duration})
            logger.info(f"{test_case['name']} is finished.")

      evaluation(failed_tests, passed_tests)
      save_results(mode, test_results)

def function_sumirize(mode):
      for test_case in user_input_test:
            logger.info(f"Test {test_case['name']} started.")
            user_input=test_case["input"]
            prompt=f"""{model_instructions["default"]} Now here is the input: {user_input}"""
            max_attempts = 3
            attempt = 0
            print(f"\n ====== Running test ======\n {test_case['name']}\n")
            start_time=time.time()

            while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)

                        cleaner_status, json_text= clean_response(raw_response)

                        if cleaner_status == False:
                              attempt+=1
                              print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt} failed.\n')
                              logger.debug(f"Attempt {attempt} failed, no JSON object found")

                              continue

                        try:
                                parsed_data=json.loads(json_text)
                                response_validated= validate_response_default(parsed_data)

                                if response_validated[0]:
                                    print(f"====== Passed ======\n{test_case['name']}\n")
                                    test_status="passed"
                                    passed_tests.append(test_case['name'])
                                    break
                                
                                else:
                                    attempt+=1
                                    logger.debug(f"Attempt {attempt} failed, validation error(s).")

                                    continue

                        except json.JSONDecodeError as e:
                                
                                attempt+=1
                                logger.debug(f"Attempt {attempt} failed, parsing error.")

                                continue
                        
            end_time=time.time()
            duration=end_time-start_time #measuring time needed for model to respond

            if attempt == max_attempts:
                        failed_tests.append(test_case['name'])
                        test_status="failed"

            logger.info(f"{test_case['name']} - {test_status}")
            test_results.append({"name":test_case['name'],"status":test_status,"attempts":attempt,"errors":response_validated[1],"duration":duration})
            logger.info(f"{test_case['name']} is finished.")

      evaluation(failed_tests, passed_tests)
      save_results(mode, test_results)
def function_rage(mode):
       
      for test_case in user_input_test:
            logger.info(f"Test {test_case['name']} started.")
            user_input=test_case["input"]
            prompt=f"""{model_instructions["default"]} Now here is the input: {user_input}"""
            max_attempts = 3
            attempt = 0
            print(f"\n ====== Running test {test_case['name']}======\n")
            start_time=time.time()

            while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)

                        cleaner_status, json_text= clean_response(raw_response)

                        if cleaner_status == False:
                              attempt+=1
                              print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt} failed.\n')
                              logger.debug(f"Attempt {attempt} failed, no JSON object found")
                              continue

                        try:
                                parsed_data=json.loads(json_text)
                                response_validated= validate_response_default(parsed_data)

                                if response_validated[0]:
                                    print(f"====== PASSED ======\n{test_case['name']}\n")
                                    passed_tests.append(test_case['name'])
                                    test_status="passed"
                                    break
                                
                                else:
                                    attempt+=1
                                    logger.debug(f"Attempt {attempt} failed, validation error(s).")
                                    print((f"====== ERROR ======\n For {test_case['name']} model returned following error(s): {response_validated[1]}\n"))
                                    continue

                        except json.JSONDecodeError as e:
                              attempt+=1
                              logger.debug(f"Attempt {attempt} failed, parsing error.")
                              print(f"====== WARNING ======\n JSON parsing failed, Error: {e}. Attempt {attempt} failed.\n")
                              continue
                        
            end_time=time.time()
            duration=end_time-start_time #measuring time needed for model to respond
            print(f"====== INFO ======\n Model response time was: {duration:.2f} seconds")

            if attempt == max_attempts:
                    
                    print("====== ERROR ======\n Maximal number of retries reached.")
                    print(f"====== WARNING ======\n Test {test_case['name']} failed.")
                    failed_tests.append(test_case['name'])
                    test_status="failed"
                    
            logger.info(f"{test_case['name']} - {test_status}")
            test_results.append({"name":test_case['name'],"status":test_status,"attempts":attempt,"errors":response_validated[1],"duration":duration})
            logger.info(f"{test_case['name']} is finished.")

      evaluation(failed_tests, passed_tests)
      save_results(mode,test_results)

def default_route(mode):

      for test_case in user_input_test:

            logger.info(f"Test {test_case['name']} started.") 
            user_input=test_case["input"]
            prompt=f"""{model_instructions["default"]} Now here is the input: {user_input}"""
            max_attempts = 3
            attempt = 0
            print(f"\n ====== Running test ======\n {test_case['name']}\n")
            start_time=time.time()

            while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)
                        cleaner_status, json_text= clean_response(raw_response)
                        if cleaner_status == False:
                              attempt+=1
                              print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt} failed.\n')
                              logger.debug(f"Attempt number {attempt} failed, no JSON object found")
                              logger.error(f"Attempt number {attempt} failed, no JSON object found")
                              continue

                        try:
                                parsed_data=json.loads(json_text)
                                response_validated= validate_response_default(parsed_data)

                                if response_validated[0]:
                                    print("====== GOAL ======\n",parsed_data.get("goal"), "\n" ) #making sure accesability is achived
                                    print("====== CONSTRAINS ======\n",parsed_data.get("constraints"), "\n")
                                    print("====== OPTIONS ======\n: ", parsed_data.get("options"), "\n")
                                    print("====== PROS AND CONS ======\n", parsed_data.get("pros_cons"), "\n")
                                    print("====== PROS AND CONS ======\n", parsed_data.get("next_steps"), "\n")
                                    print(parsed_data.get("cheer"), "\n")
                                    passed_tests.append(test_case['name'])
                                    test_status="passed"
                                    break
                                
                                else:
                                    logger.debug(f"Attempt {attempt} failed, validation error.")
                                    logger.error(f"{test_case['name']} had following validation errors:{response_validated[1]}")
                                    attempt+=1
                                    continue

                        except json.JSONDecodeError as e:
                              logger.debug(f"Attempt {attempt} failed, parsing error.")
                              logger.error(f"Parsing error: {e}, preview:{raw_response[:200]}")
                              attempt+=1
                              continue
                        
            end_time=time.time()
            duration=end_time-start_time

            if attempt == max_attempts:

                    failed_tests.append(test_case['name'])
                    logger.error(f"Max attempts ({attempt}) reached for {test_case['name']}")
                    test_status="failed"

            logger.info(f"{test_case['name']} - {test_status}")
            test_results.append({"name":test_case['name'],"status":test_status,"attempts":attempt,"errors":response_validated[1],"duration":duration})
            logger.info(f"{test_case['name']} is finished.")


      evaluation(failed_tests, passed_tests)
      save_results(mode,test_results)


def route_mode(mode):

      handlers={
            "plan":function_plan,
            "sumirize":function_sumirize,
            "rage":function_rage,
            "test":function_test,
            }
      if mode in handlers:
            handlers[mode](mode)
            return True
      else:
            print(f"====== ERROR ======\n Invalid mode: {mode}")
            return None
      
def is_valid_log_level(llevel):
      if llevel not in allowed_log_levels:
            return False
      else:
            return True



    




