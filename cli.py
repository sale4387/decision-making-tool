import argparse
from config import allowed_log_levels, PRIMARY_MODEL_PROVIDER, SECONDARY_MODEL_PROVIDER, MODEL_MAP,AUDIO_FILE, USER_INPUT
from validation import validate_response_default, validate_response_partial
import logging
from functions import init_test_case, finalize_test_run, prepare_test_case,process_test_results, run_test_case, convert_voice_to_text
from model import HFClient, GEMINIClient
logger=logging.getLogger(__name__)


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode")
    parser.add_argument("-l", "--llevel")
    args = parser.parse_args()
    return args.mode, args.llevel.upper() if args.llevel else None

def default_route(mode):

      test_results,session, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode=init_test_case(mode)
      fallback="no"
      user_input=USER_INPUT
            
      prompt=prepare_test_case(user_input,input_based_on_mode, mode)

      test_status, parsed_data, duration, error_type, number_of_tries, validation_errors, model_calls,test_score = run_test_case(primary_client, prompt, validate_response_default, user_input)
      provider=PRIMARY_MODEL_PROVIDER

      if test_status=="failed":
            logger.info(f"Test with {PRIMARY_MODEL_PROVIDER} failed due to {error_type} after {number_of_tries} tries, trying with {SECONDARY_MODEL_PROVIDER}")
            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors,model_calls,test_score=run_test_case(secondary_client, prompt, validate_response_default,user_input)
            provider=SECONDARY_MODEL_PROVIDER
            fallback="yes"
            if error_type:
                        ERROR_COUNTS[error_type] += 1

                  
      process_test_results(test_status,test_results,session,mode, user_input, number_of_tries, error_type,validation_errors, duration,parsed_data, provider, model_calls,fallback,test_score)
      if error_type:
                        ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS,mode,test_results,session)
             

def function_summary(mode):

      test_results,session, ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode=init_test_case(mode)

            
      user_input=USER_INPUT

            
      prompt=prepare_test_case(user_input,input_based_on_mode, mode)
            
      test_status, parsed_data, duration, error_type, number_of_tries, validation_errors,model_calls = run_test_case(primary_client, prompt, validate_response_default)
            
      if parsed_data:
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )
                  print("====== CATEGORY ======\n",parsed_data.get("category"), "\n" )


      process_test_results(test_status,test_results,session,mode, user_input, number_of_tries, error_type,validation_errors, duration,parsed_data,PRIMARY_MODEL_PROVIDER,model_calls)
            
      if error_type:
            ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS,mode,test_results,session)


def function_voice(mode):

      test_results,session,ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode=init_test_case(mode)
      
      user_input=convert_voice_to_text(AUDIO_FILE)
            
      prompt=prepare_test_case(user_input,input_based_on_mode, mode)

      test_status, parsed_data, duration, error_type, number_of_tries, validation_errors,model_calls = run_test_case(primary_client, prompt, validate_response_default)
      if parsed_data:
                  print("====== GOAL ======\n",parsed_data.get("goal"), "\n" )
                  print("====== CATEGORY ======\n",parsed_data.get("category"), "\n" )
                  print("====== OPTIONS ======\n",parsed_data.get("options"), "\n" )
                  print("====== LIMITATIONS ======\n",parsed_data.get("constraints"), "\n" )
                  print("====== PROS AND CONS ======\n",parsed_data.get("pros_cons"), "\n" )
                  print("====== NEXT STEPS ======\n",parsed_data.get("next_steps"), "\n" )
                  print(parsed_data.get("cheer"), "\n" )


      process_test_results(test_status,test_results, session, mode, user_input, number_of_tries, error_type, validation_errors, duration, parsed_data, PRIMARY_MODEL_PROVIDER, model_calls)            
              
      if error_type:
            ERROR_COUNTS[error_type] += 1

      finalize_test_run(ERROR_COUNTS,mode,test_results,session)


def function_compare(mode):

      hf_client=HFClient(MODEL_MAP["huggingface"])
      gemini_client=GEMINIClient(MODEL_MAP["google"]) 
      test_results,session,ERROR_COUNTS,primary_client, secondary_client, input_based_on_mode=init_test_case(mode)

      user_input=USER_INPUT
            
      prompt=prepare_test_case(user_input,input_based_on_mode, mode)

      test_status_hf, parsed_data_hf, duration_hf,error_type_hf,retries_hf,validation_errors_hf  = run_test_case(hf_client, prompt, validate_response_partial)
      test_status_g, parsed_data_g, duration_g,error_type_g,retries_g,validation_errors_g = run_test_case(gemini_client, prompt, validate_response_partial)

      print(f"=====STATUS=====\n{test_status_hf}")
      print(f"=====DURATION=====\n{duration_hf}s")
      print(f"=====ERRORS=====\n{error_type_hf}")
      if parsed_data_hf:
            print("====== GOAL ======\n",parsed_data_hf.get("goal"), "\n" )
            print("====== CATEGORY ======\n",parsed_data_hf.get("category"), "\n" )
            print("====== OPTIONS ======\n",parsed_data_hf.get("options"), "\n" )
            print("====== LIMITATIONS ======\n",parsed_data_hf.get("constraints"), "\n" )
            print("====== PROS AND CONS ======\n",parsed_data_hf.get("pros_cons"), "\n" )
            print("====== NEXT STEPS ======\n",parsed_data_hf.get("next_steps"), "\n" )
            print(parsed_data_hf.get("cheer"), "\n" )

      print(f"=====STATUS=====\n{test_status_g}")
      print(f"=====DURATION=====\n{duration_g}s")
      print(f"=====ERRORS=====\n{error_type_g}")

      if parsed_data_g:
            print(f"===== GOAL =====\n" ,parsed_data_g.get("goal"), "\n")
            print("====== CATEGORY ======\n",parsed_data_g.get("category"), "\n" )
            print("====== OPTIONS ======\n",parsed_data_g.get("options"), "\n" )
            print("====== LIMITATIONS ======\n",parsed_data_g.get("constraints"), "\n" )
            print("====== PROS AND CONS ======\n",parsed_data_g.get("pros_cons"), "\n" )
            print("====== NEXT STEPS ======\n",parsed_data_g.get("next_steps"), "\n" )
            print(parsed_data_hf.get("cheer"), "\n" )

def route_mode(mode):

      handlers={
            "summary":function_summary,
            "compare":function_compare,
            "voice":function_voice
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



    




