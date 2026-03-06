
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
            "content": "Return your reply in valid JSON format only with following keys: goal(string), constraints (array of strings), options (array of strings), pros_cons (object which should list options which are also object. under each option we have two arrays pros[] and cons[]. under each of those two array we should have 3-5 elements), next_steps (array of strings). Now here is the input: My friend Misha is thinking about moving to Amsterdam but he is not sure that is a good moment. He is from Smederevo and he likes to visit his family on weekends, hang out with his friends and visit Menza AKA Butik 3 restaurant. His main concern is that living costs are higher in NL than in RS and standard of living will mostly deopend on him finding a job. he really needs some guidence on what to do what things should he compare and pros and cons but he cant organize his thoughts and he doesnt know which next step to take"
        }
    ],
)

raw = completion.choices[0].message.content.strip()

start = raw.find("{")
end = raw.rfind("}")

if start == -1 or end == -1:
    raise ValueError("No JSON object found in model output")

raw_json = raw[start:end+1]
data = json.loads(raw_json)




