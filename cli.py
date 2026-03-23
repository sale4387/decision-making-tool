import argparse
from model import call_model
from config import user_input_test, model_instructions, model_instructions_plan
import time
from model import call_model
import json
from logger import logger
from validation import validate_response_default, validate_responce_partial
from model import call_model
from evaluation import evaluation
from cleaner import clean_response

failed_tests=[]
passed_tests=[]

def get_mode():

      parser = argparse.ArgumentParser()
      parser.add_argument("-m", "--mode")
      args = parser.parse_args()
      mode = args.mode
      logger.info(f"CLI mode selected: {mode}")
      return mode

def function_plan():

      for test_case in user_input_test:

            user_input = test_case["input"]
            prompt= f"{model_instructions_plan} Now here is the input: {user_input}"
            max_attempts = 3
            attempt = 0
            print(f"\n ====== Running test: ======\n {test_case['name']}\n")
            start_time=time.time()

            while attempt < max_attempts:
                  raw_response=call_model(prompt)

                  cleaner_status, json_text= clean_response(raw_response)

                  if cleaner_status == False:
                        logger.warning(f'No JSON object found in model response. Attempt {attempt+1} failed.')
                        print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt+1} failed.\n')
                        attempt+=1
                        continue

                  try:
                      parsed_data=json.loads(json_text)
                      response_validated = validate_responce_partial(parsed_data)

                      if response_validated[0]:
                            print("====== GOAL ======")
                            print(parsed_data.get("goal"), "\n" )
                            print("====== OPTIONS ======\n")
                            print(parsed_data.get("options"), "\n")
                            print("====== NEXT STEPS ======\n")
                            print(parsed_data.get("next_steps"), "\n")
                            logger.info(f"{test_case['name']} passed")
                            passed_tests.append(test_case['name'])
                            break
                      
                      else:
                        logger.error(f"For {test_case['name']} model returned following error(s): {response_validated[1]}")
                        attempt+=1
                        continue
                      
                  except json.JSONDecodeError as e:
                        logger.warning(f"JSON parsing failed, Error: {e}. Attempt {attempt+1} failed.")
                        logger.info(f"Response preview: {raw_response[:200]}") # handling exact error for easier debugging later
                        attempt+=1
                        continue

            end_time=time.time()
            duration=end_time-start_time #measuring time needed for model to respond
            logger.info(f"Model response time was: {duration:.2f} seconds")
            
            if attempt == max_attempts:
                  logger.error("Maximal number of retries reached.")
                  logger.warning(f"test {test_case['name']} failed.")
                  failed_tests.append(test_case['name'])

      evaluation(failed_tests, passed_tests)


def function_sumirize():
      for test_case in user_input_test:
                
                user_input=test_case["input"]
                prompt=f"""{model_instructions} Now here is the input: {user_input}"""
                max_attempts = 3
                attempt = 0
                print(f"\n ====== Running test ======\n {test_case['name']}\n")
                start_time=time.time()

                while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)

                        cleaner_status, json_text= clean_response(raw_response)

                        if cleaner_status == False:
                              logger.warning(f'No JSON object found in model response. Attempt {attempt+1} failed.')
                              print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt+1} failed.\n')
                              attempt+=1
                              continue

                        try:
                                parsed_data=json.loads(json_text)
                                response_validated= validate_response_default(parsed_data)

                                if response_validated[0]:
                                    logger.info(f"test {test_case['name']} passed.")
                                    print(f"====== Passed ======\n{test_case['name']}\n")

                                    passed_tests.append(test_case['name'])
                                    break
                                
                                else:
                                    logger.error(f"For {test_case['name']} model returned following error(s): {response_validated[1]}")
                                    attempt+=1
                                    continue

                        except json.JSONDecodeError as e:
                                
                                logger.warning(f"JSON parsing failed, Error: {e}. Attempt {attempt+1} failed.")
                                logger.info(f"Response preview: {raw_response[:200]}") # handling exact error for easier debugging later
                                attempt+=1
                                continue
                        
                end_time=time.time()
                duration=end_time-start_time #measuring time needed for model to respond
                logger.info(f"Model response time was: {duration:.2f} seconds")

                if attempt == max_attempts:
                    
                    logger.error("Maximal number of retries reached.")
                    logger.warning(f"test {test_case['name']} failed.")
                    failed_tests.append(test_case['name'])

      evaluation(failed_tests, passed_tests)

def function_rage():
       
      for test_case in user_input_test:
                
                user_input=test_case["input"]
                prompt=f"""{model_instructions} Now here is the input: {user_input}"""
                max_attempts = 3
                attempt = 0
                print(f"\n ====== Running test {test_case['name']}======\n")
                start_time=time.time()

                while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)

                        cleaner_status, json_text= clean_response(raw_response)

                        if cleaner_status == False:
                              logger.warning(f'No JSON object found in model response. Attempt {attempt+1} failed.')
                              print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt+1} failed.\n')
                              attempt+=1
                              continue

                        try:
                                parsed_data=json.loads(json_text)
                                response_validated= validate_response_default(parsed_data)

                                if response_validated[0]:
                                    logger.info(f"test {test_case['name']} passed.")
                                    print(f"====== PASSED ======\n{test_case['name']}\n")
                                    passed_tests.append(test_case['name'])
                                    break
                                
                                else:
                                    logger.error(f"For {test_case['name']} model returned following error(s): {response_validated[1]}")
                                    print((f"====== ERROR ======\n For {test_case['name']} model returned following error(s): {response_validated[1]}\n"))
                                    attempt+=1
                                    continue

                        except json.JSONDecodeError as e:
                                
                                logger.warning(f"JSON parsing failed, Error: {e}. Attempt {attempt+1} failed.")
                                print(f"====== WARNING ======\n JSON parsing failed, Error: {e}. Attempt {attempt+1} failed.\n")
                                logger.info(f"Response preview: {raw_response[:200]}") # handling exact error for easier debugging later
                                attempt+=1
                                continue
                        
                end_time=time.time()
                duration=end_time-start_time #measuring time needed for model to respond
                logger.info(f"Model response time was: {duration:.2f} seconds")
                print(f"====== INFO ======\n Model response time was: {duration:.2f} seconds")

                if attempt == max_attempts:
                    
                    logger.error("Maximal number of retries reached.")
                    print("====== ERROR ======\n Maximal number of retries reached.")
                    logger.warning(f"test {test_case['name']} failed.")
                    print(f"====== WARNING ======\n Test {test_case['name']} failed.")
                    failed_tests.append(test_case['name'])

      evaluation(failed_tests, passed_tests)

def default_route():

      for test_case in user_input_test:
                
                user_input=test_case["input"]
                prompt=f"""{model_instructions} Now here is the input: {user_input}"""
                max_attempts = 3
                attempt = 0
                print(f"\n ====== Running test ======\n {test_case['name']}\n")
                start_time=time.time()

                while attempt < max_attempts:
                        
                        raw_response=call_model(prompt)

                        cleaner_status, json_text= clean_response(raw_response)

                        if cleaner_status == False:
                              logger.warning(f'No JSON object found in model response. Attempt {attempt+1} failed.')
                              print(f'====== WARNING ======\n No JSON object found in model response. Attempt {attempt+1} failed.\n')
                              attempt+=1
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
                                    logger.info(f"test {test_case['name']} passed.")
                                    passed_tests.append(test_case['name'])
                                    break
                                
                                else:
                                    logger.error(f"For {test_case['name']} model returned following error(s): {response_validated[1]}")
                                    attempt+=1
                                    continue

                        except json.JSONDecodeError as e:
                                logger.warning(f"JSON parsing failed, Error: {e}. Attempt {attempt+1} failed.")
                                logger.info(f"Response preview: {raw_response[:200]}") 
                                attempt+=1
                                continue
                        
                end_time=time.time()
                duration=end_time-start_time
                logger.info(f"Model response time was: {duration:.2f} seconds")

                if attempt == max_attempts:
                    logger.error("Maximal number of retries reached.")
                    logger.warning(f"test {test_case['name']} failed.")
                    failed_tests.append(test_case['name'])

      evaluation(failed_tests, passed_tests)


def route_mode(mode):

      handlers={
            "plan":function_plan,
            "sumirize":function_sumirize,
            "rage":function_rage,
            }
      if mode in handlers:
            handlers[mode]()
            return True
      else:
            print(f"====== ERROR ======\n Invalid mode: {mode}")
            return None


    




