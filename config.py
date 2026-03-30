import os


HF_TOKEN=os.getenv("HF_TOKEN")
MODEL_NAME="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai"
MODEL_PROVIDER = "huggingface"

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2
MODEL_TIMEOUT = 60

LOG_LEVEL = "INFO"

allowed_log_levels=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

TEMPERATURE = 0.3
MAX_TOKENS = 800
TOP_P = 0.9

required_keys ={
    "default":
      [
        "goal",
        "constraints",
        "options",
        "pros_cons",
        "next_steps",
        "cheer"
      ],
    "plan":
      [
        "goal",
        "options",
        "next_steps",
        "cheer" 
      ]
}

validation_rules={
 "constraints":(3,6),  
 "options": (2,4),
 "pros":(3,5),
 "cons":(3,5),
 "next_steps":(3,5)
}



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

model_instructions ={
    "default":
      """
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
        }
      """,
    "plan":
      """
          Return your reply in VALID JSON ONLY. Do not include explanations, markdown, or text outside JSON.

          The JSON must contain exactly these keys:

          goal: string

          options: array of option names as strings (2–4 items)

          next_steps: array of strings (3–5 actionable steps)

          cheer: string (short encouraging message)

          Example structure:

          {
            "goal": "...",
            "options": ["option A", "option B"],
            "next_steps": ["...", "..."],
            "cheer": "..."
          }
      """
}
