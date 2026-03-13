
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
import json
import logging
import time

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


client = InferenceClient(
    api_key=os.getenv("HF_TOKEN"),
)
model_name="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai"
def call_model(prompt):
        completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
                }#content is actual prompt
        ],)
        
        raw = completion.choices[0].message.content.strip()
        return raw



required_keys = [
    "goal",
    "constraints",
    "options",
    "pros_cons",
    "next_steps",
    "cheer"
]

min_len_constraints = 3
max_len_constraints = 6
min_len_options = 2
max_len_options = 4
min_len_pros = 3
max_len_pros = 5
min_len_cons= 3
max_len_cons= 5
min_len_next_steps = 3
max_len_next_steps = 5

def validate_response(parsed_data):
    error_log_message=[]
    for key in required_keys:
        if key not in parsed_data:
            error_log_message.append(f"A key is missing from parsed data.\n")
    if not min_len_constraints <= len(parsed_data["constraints"]) <= max_len_constraints:
             error_log_message.append(f"Number of constraints is wrong.\n")
    if not min_len_options <= len(parsed_data["options"]) <= max_len_options:
             error_log_message.append(f"Number of options is wrong.\n")
    if not min_len_next_steps <= len(parsed_data["next_steps"]) <= max_len_next_steps:
             error_log_message.append(f"Number of next steps is wrong.\n")
    for opt in parsed_data["pros_cons"]:
          pros = parsed_data["pros_cons"][opt]["pros"]
          cons = parsed_data["pros_cons"][opt]["cons"]
          if not min_len_pros <= len(pros) <= max_len_pros:
                error_log_message.append(f"Number of pros is wrong.\n")
          if not min_len_cons <= len(cons) <= max_len_cons:
                error_log_message.append(f"Number of cons is wrong.\n")
    if set(parsed_data["options"]) != set(parsed_data["pros_cons"].keys()):
          error_log_message.append(f"Option set not matching Pros and Cons keys.\n")
    if error_log_message:
          return [False, error_log_message]
    else:
          return [True, error_log_message]
    

input1="""Constant market changes, pressure to get results, wars, expansion of AI and personal feeling of no motivation in current job are every day concerns for me. Also during covid expecialy i was thinking a lot about starting to do something with my hands. During renovation of my own appartment and later with moving to NL i realized that for example laying tiles is well paid job, not an easy one abut the one that can be learned as anything else with practice. Initialy i would do some work for myself but who knows, maybe it can be occasional source of income. I did a lot of reserach and theory is not the problem what pesrson needs to do is to give it a try make mistakes and learn from them. It would be great if there is a way for mistakes not to be expensive ones"""
input2="""I am still on HSM visa in NL, 1st of Aug 27 i ll be eligeble to apply for permanent visa and later passport. AS i ll lose 30 percent rulling on kid is in kindergarten another to be born in june i am thinking about my situation once i get the passport. Also have a house i nl probably i ll make nice profit in two years from now or so and i always wanted to go to live in spain too... depending on job situation and profit with house if i can by real estate in valencia or similar with that profit could be interesting story. On the other hand better job market and living standard is in NL"""
input3="""Since may last year i did a course on Dutch language, passed a1 and a2 exams but i got a bit tired of it...going to clases and learing on class was easy but doing homework was too much to me so i made a break.. I want to learn maybe b1 level so i can be able to speak with peopel and use this skill really to apply for jobs and be better candidate. However i need to pass inburgering too so after my pause i need to decide whatever i should prepare inburgering and then think of starting b1 or to start b1 and do inburgering while going going to b1"""
input4="""My contract with Odido NL will expeire on 13th of april and i have pixel 8 phone which i need to by out from them for 200 eur if i want t okeep it...option is to return it and to get cca 100 eur but i am not sure...as i am not really a phone guy and i dont like spending money on phones not really sure if i want to deal with it looking for new phone or simply to keep this one and pay 200 eur"""
input5="""My cat annual bill for vet is 72 eur which includes vacination and yearly check up...but this year she had anemia so we spend cca 400 eur on top of vaccination. i am thinking whatever it is a good idea to get insurance which i ll have to pay up to 25 eur per month"""

user_input_test = [
     
    {"name": "job_change", "input":input1},
    {"name": "move_country", "input":input2},
    {"name": "learn_dutch", "input":input3},
    {"name": "phone_situation", "input":input4},
    {"name": "cat_costs", "input":input5},
]

model_instructions = """
Return your reply in VALID JSON ONLY. Do not include explanations, markdown, or text outside JSON.

The JSON must contain exactly these keys:

goal: string

constraints: array of strings (3–6 items)

options: array of option names as strings (2–4 items)

pros_cons: object where each key matches an option name from "options".
Each option must contain:
    pros: array of strings (3–5 items)
    cons: array of strings (3–5 items)

next_steps: array of strings (3–5 actionable steps)

cheer: string (short encouraging message)

Example structure:

{
  "goal": "...",
  "constraints": ["...", "..."],
  "options": ["option A", "option B"],
  "pros_cons": {
    "option A": {
      "pros": ["...", "..."],
      "cons": ["...", "..."]
    },
    "option B": {
      "pros": ["...", "..."],
      "cons": ["...", "..."]
    }
  },
  "next_steps": ["...", "..."],
  "cheer": "..."
}
"""
failed_tests=[]
passed_tests=[]




for test_case in user_input_test:
    user_input=test_case["input"]
    prompt=f"""{model_instructions} Now here is the input: {user_input}"""
    max_attempts = 3
    attempt = 0
    print(f"\nRunning test: {test_case['name']}")
    start_time=time.time()
    while attempt < max_attempts:
            raw_response = call_model(prompt)
 
            start = raw_response.find("{")
            end = raw_response.rfind("}")
            if start == -1 or end == -1: #Checking if { or } are missing
                logger.error(f'No JSON object found in model response. Attempt {attempt+1} failed.')

                attempt+=1
                continue

            json_text= raw_response[start : end+1] # creating new response format making sure starts with { and ends with}

            try:
                    parsed_data=json.loads(json_text)
                    response_validated= validate_response(parsed_data)
                    if response_validated[0]:
                        """print("Goal: ",parsed_data.get("goal"), "\n" ) #making sure accesability is achived
                        print("Constraints: ",parsed_data.get("constraints"), "\n")
                        print("Options: ", parsed_data.get("options"), "\n")
                        print("Pros/Cons: ", parsed_data.get("pros_cons"), "\n")
                        print("Next steps: ", parsed_data.get("next_steps"), "\n")
                        print(parsed_data.get("cheer"), "\n")"""
                        logger.info(f"test {test_case['name']} passed.")
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
        logger.info(f"test {test_case['name']} failed.")
        failed_tests.append(test_case['name'])

total_failed_tests=len(failed_tests)
total_passed_tests=len(passed_tests)
total_tests=total_failed_tests+total_passed_tests
print(f"Failed tests: ",failed_tests, "\n")
print(f"Passed tests",passed_tests, "\n")
print(f"Total tests:", total_tests)

with open ("eval_results.log", "w") as file:
     total_tests_string = repr(total_tests)
     total_passed_tests_string=repr(total_passed_tests)
     total_failed_tests_string=repr(total_failed_tests)
     file.write("Number of total tests was:" + total_tests_string +".\n")
     file.write("Number of passed tests was:" + total_passed_tests_string +".\n")
     file.write("Number of failed tests was:" + total_failed_tests_string +".\n")

