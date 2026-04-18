import argparse
from config import user_input_test, allowed_log_levels, PRIMARY_MODEL_PROVIDER, SECONDARY_MODEL_PROVIDER, MODEL_MAP
from validation import validate_response_default, validate_response_partial, validate_response_minimal
import logging
from functions import init_test_case, finalize_test_run, prepare_test_case,process_test_results, run_test_case, PROVIDER_MAP
from model import HFClient, GEMINIClient
logger=logging.getLogger(__name__)


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode")
    parser.add_argument("-l", "--llevel")
    args = parser.parse_args()
    return args.mode, args.llevel.upper() if args.llevel else None


            
def function_test(mode):
      total_tries=0
      total_duration=0

      
      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode,test_summary=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)

            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors= run_test_case(primary_client, prompt, validate_response_minimal)
            
            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, number_of_tries, error_type,validation_errors, duration,parsed_data, PRIMARY_MODEL_PROVIDER)
            total_tries+=number_of_tries
            total_duration+=duration

            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session, total_tries, total_duration, test_summary)

def function_failover(mode):
      total_tries=0
      total_duration=0
      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode,test_summary=init_test_case(mode)

      for test_case in user_input_test:

            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)

            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors = run_test_case(primary_client, prompt, validate_response_default)
            provider=PRIMARY_MODEL_PROVIDER

            if test_status=="failed":
                  logger.info(f"Test with {PRIMARY_MODEL_PROVIDER} failed, trying with {SECONDARY_MODEL_PROVIDER}")
                  test_status, parsed_data, duration, error_type, number_of_tries, validation_errors=run_test_case(secondary_client, prompt, validate_response_default)
                  provider=SECONDARY_MODEL_PROVIDER


            if parsed_data:
                  print(f"======={test_name}=======")
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )
                  print("====== OPTIONS ======\n",parsed_data.get("options"), "\n" )
                  print("====== LIMITATIONS ======\n",parsed_data.get("constraints"), "\n" )
                  print("====== PROS AND CONS ======\n",parsed_data.get("pros_cons"), "\n" )
                  print("====== NEXT STEPS ======\n",parsed_data.get("next_steps"), "\n" )
                  print(parsed_data.get("cheer"), "\n" )

            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, number_of_tries, error_type,validation_errors, duration,parsed_data, provider)
            total_tries+=number_of_tries
            total_duration+=duration
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session, total_tries, total_duration, test_summary)


def function_summary(mode):
      total_tries=0
      total_duration=0
      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode,test_summary=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors = run_test_case(primary_client, prompt, validate_response_default)
            
            if parsed_data:
                  print(f"======={test_name}=======")
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )

            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, number_of_tries, error_type,validation_errors, duration,parsed_data,PRIMARY_MODEL_PROVIDER)
            
            total_tries+=number_of_tries
            total_duration+=duration

            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session, total_tries, total_duration, test_summary)


def function_rage(mode):
      total_tries=0
      total_duration=0
      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode,test_summary=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors = run_test_case(primary_client, prompt, validate_response_default)
            
            if parsed_data:
                  print(f"======={test_name}=======")
                  print(f"======VALIDATION ERRORS======\n{validation_errors}")
                  print(f"======DURATION======\n{duration} sec.")


            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests,test_results,session,mode, user_input, number_of_tries, error_type,validation_errors, duration,parsed_data, PRIMARY_MODEL_PROVIDER)
            
            total_tries+=number_of_tries
            total_duration+=duration
   
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session, total_tries, total_duration, test_summary)

def default_route(mode):

      total_tries=0
      total_duration=0

      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode,test_summary=init_test_case(mode)

      for test_case in user_input_test:
            
            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors = run_test_case(primary_client, prompt, validate_response_default)
            if parsed_data:
                  print(f"======={test_name}=======")
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )
                  print("====== OPTIONS ======\n",parsed_data.get("options"), "\n" )
                  print("====== LIMITATIONS ======\n",parsed_data.get("constraints"), "\n" )
                  print("====== PROS AND CONS ======\n",parsed_data.get("pros_cons"), "\n" )
                  print("====== NEXT STEPS ======\n",parsed_data.get("next_steps"), "\n" )
                  print(parsed_data.get("cheer"), "\n" )


            process_test_results(test_name, test_status, test_case, category_results, passed_tests, failed_tests, test_results, session, mode, user_input, number_of_tries, error_type, validation_errors, duration, parsed_data, PRIMARY_MODEL_PROVIDER)            
            
            total_tries+=number_of_tries
            total_duration+=duration

            
            if error_type:
                  ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS, category_results, failed_tests,passed_tests,mode,test_results,session, total_tries, total_duration, test_summary)


def function_compare(mode):

      total_tries=0
      total_duration=0

      hf_client=HFClient(MODEL_MAP["huggingface"])
      gemini_client=GEMINIClient(MODEL_MAP["google"]) 
      failed_tests, passed_tests, test_results,session, category_results, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode=init_test_case(mode)

      for test_case in user_input_test:
            

            test_name, user_input, prompt=prepare_test_case(test_case, input_based_on_mode)
            test_status_hf, parsed_data_hf, duration_hf, error_type_hf, number_of_tries_hf, validation_errors_hf = run_test_case(hf_client, prompt, validate_response_partial)
            test_status_g, parsed_data_g, duration_g, error_type_g, number_of_tries_g, validation_errors_g = run_test_case(gemini_client, prompt, validate_response_partial)

            print(f"======={test_name} - HF =======")
            print(f"=====STATUS=====\n{test_status_hf}")
            print(f"=====DURATION=====\n{duration_hf}")
            if parsed_data_hf:
                  print("====== GOAL ======\n",parsed_data_hf.get("goal"), "\n" )


            print(f"======={test_name} - Gemini =======")
            print(f"=====STATUS=====\n{test_status_g}")
            print(f"=====DURATION=====\n{duration_g}")
            if parsed_data_g:
                  print(f"===== GOAL =====\n" ,parsed_data_g.get("goal"), "\n")




def route_mode(mode):

      handlers={
            "failover":function_failover,
            "summary":function_summary,
            "rage":function_rage,
            "test":function_test,
            "compare":function_compare
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



    




