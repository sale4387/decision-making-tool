from fastapi import FastAPI, Request
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
from functions import prepare_test_case, init_test_case, run_test_case, process_test_results, finalize_test_run, is_rate_limited
from config import PRIMARY_MODEL_PROVIDER, SECONDARY_MODEL_PROVIDER
from validation import validate_response_default
import time

class Request(BaseModel):
    user_input: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/decision")
def decision(request:Request):
 

    start_time = time.time()
    isFallback="no"
    primary_error_type=None
    primary_validation_error=None
    primary_retries=None
    primary_parsed_data=None
    provider=PRIMARY_MODEL_PROVIDER

    test_results,session,primary_client, secondary_client, input_based_on_mode=init_test_case("default")
    prompt=prepare_test_case(request.user_input, input_based_on_mode,"default")
    test_status, parsed_data, duration, error_type, number_of_tries, validation_errors, model_calls,test_score = run_test_case(primary_client, prompt, validate_response_default, request.user_input)



    if test_status=="failed":
            
            primary_error_type=error_type
            primary_validation_error=validation_errors
            primary_retries=number_of_tries
            primary_parsed_data=parsed_data
            provider=SECONDARY_MODEL_PROVIDER
            isFallback="yes"

            test_status, parsed_data, duration, error_type, number_of_tries, validation_errors, model_calls,test_score = run_test_case(secondary_client, prompt, validate_response_default, request.user_input)

            if test_status=="failed":
                 parsed_data=None

    process_test_results(test_status,test_results,session,"default", request.user_input, number_of_tries, error_type,validation_errors, duration,parsed_data,PRIMARY_MODEL_PROVIDER,model_calls,isFallback,test_score)
    finalize_test_run("default",test_results,session)
    end_time = time.time()
    total_duration = f"{end_time - start_time:.2f}"
    return {
              "data":parsed_data,
              "status":test_status,
              "provider":provider,
              "duration":duration,
              "retries":number_of_tries,
              "error":error_type,
              "errors":validation_errors,
              "calls":model_calls,
              "quality":test_score,
              "fallback":isFallback,
              "total_duration":total_duration,
              "primary":{
                   "data":primary_parsed_data,
                   "error":primary_error_type,
                   "errors":primary_validation_error,
                   "retries":primary_retries
              }

              }

                   
              





    