import argparse
from config import user_input_test, allowed_log_levels
from validation import validate_response_default, validate_response_partial, validate_response_minimal
import logging
from functions import init_test_case, finalize_test_run, prepare_test_case,process_test_results, run_test_case

logger=logging.getLogger(__name__)



def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode")
    parser.add_argument("-l", "--llevel")
    args = parser.parse_args()
    return args.mode, args.llevel.upper() if args.llevel else None



            
def function_test(mode):
      
      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,client, input_based_on_mode=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)

            test_status, parsed_data, duration, error_type, attempt, validation_errors = run_test_case(client, prompt, validate_response_minimal)
            
            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, attempt, error_type,validation_errors, duration,parsed_data)
            
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session)

def function_plan(mode):

      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,client, input_based_on_mode=init_test_case(mode)

      for test_case in user_input_test:
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)

            test_status, parsed_data, duration, error_type, attempt, validation_errors = run_test_case(client, prompt, validate_response_partial)
            
            if parsed_data:
                  print(f"======={test_name}=======")
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )
                  print("====== OPTIONS ======\n",parsed_data.get("options"), "\n" )
                  print("====== NEXT STEPS ======\n",parsed_data.get("next_steps"), "\n" ) 

            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, attempt, error_type,validation_errors, duration,parsed_data)
            
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session)



def function_summirize(mode):

      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,client, input_based_on_mode=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status, parsed_data, duration, error_type, attempt, validation_errors = run_test_case(client, prompt, validate_response_default)
            
            if parsed_data:
                  print(f"======={test_name}=======")
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )

            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, attempt, error_type,validation_errors, duration,parsed_data)
            
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session)


def function_rage(mode):

      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,client, input_based_on_mode=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status, parsed_data, duration, error_type, attempt, validation_errors = run_test_case(client, prompt, validate_response_default)
            
            if parsed_data:
                  print(f"======={test_name}=======")
                  print(f"======VALIDATION ERRORS======\n{validation_errors}")
                  print(f"======DURATION======\n{duration} sec.")


            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, attempt, error_type,validation_errors, duration,parsed_data)
            
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session)

def default_route(mode):

      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,client, input_based_on_mode=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status, parsed_data, duration, error_type, attempt, validation_errors = run_test_case(client, prompt, validate_response_default)
            if parsed_data:
                  print(f"======={test_name}=======")
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )
                  print("====== OPTIONS ======\n",parsed_data.get("options"), "\n" )
                  print("====== LIMITATIONS ======\n",parsed_data.get("constraints"), "\n" )
                  print("====== PROS AND CONS ======\n",parsed_data.get("pros_cons"), "\n" )
                  print("====== NEXT STEPS ======\n",parsed_data.get("next_steps"), "\n" )
                  print(parsed_data.get("cheer"), "\n" )


            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, attempt, error_type,validation_errors, duration,parsed_data)
            
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session)


def route_mode(mode):

      handlers={
            "plan":function_plan,
            "summirize":function_summirize,
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



    




