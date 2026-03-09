
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
import json
import logging
import time

load_dotenv()

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


client = InferenceClient(
    api_key=os.getenv("HF_TOKEN"),
)
user_input = input("Describe your problem: ")
prompt=f"""Return your reply in valid JSON format only with following keys: goal(string), constraints (array of strings), options (array of strings), pros_cons (object which should list options which are also object. under each option we have two arrays pros[] and cons[]. under each of those two array we should have 3-5 elements), next_steps (array of strings). Now here is the input: {user_input}"""
start_time=time.time()
completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": prompt
            }#content is actual prompt
    ],
)
end_time=time.time()
raw_responce = completion.choices[0].message.content.strip() # removing whitespaces
start = raw_responce.find("{")
end = raw_responce.rfind("}")
if start == -1 or end == -1: #Checking if { or } are missing
    logger.error('No JSON object found in model response.')

else:

    json_text= raw_responce[start : end+1] # creating new responce format making sure starts with { and ends with}

    try:
        parsed_data=json.loads(json_text)
        print(parsed_data["goal"]) #making sure accesability is achived
        print(parsed_data["constraints"])
        print(parsed_data["options"])
   

    except json.JSONDecodeError as e:
        print("Invalid JSON returned by model: ", e) # handling exact error for easier debugging later

duration=end_time-start_time
logger.info(f"Time passed was {duration} seconds")




