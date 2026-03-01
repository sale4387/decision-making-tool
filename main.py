
from dotenv import load_dotenv
load_dotenv()

import os
from huggingface_hub import InferenceClient
import json
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": "I am looking to change my career focus and improve my skillset. I also want to be able to adjust my cv so i can apply for jobs which mean working with AI. While AI is still a thing i want to try to get on it ahead the curve. I passed promts course and some basic python and i managed to build some simple API which showed me city name and temperature based on coordinates only. It actually combined two apis. In order to get familiar with it i want to build my own tool. I often use chatgpt to collect info and to get help by choosing between alternatives. i often dont know much around the topic so i started broadly give a lot of context so it is good to have a tool which will 1st summiraze my thoughts and help me get to next steps such as defining budgets and picking alternatives"
        }
    ],
)

#print(completion.choices[0].message.content)

print(completion.__dict__.keys())