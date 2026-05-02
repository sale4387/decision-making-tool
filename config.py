import os

HF_TOKEN=os.getenv("HF_TOKEN")
PRIMARY_MODEL_PROVIDER = "huggingface"
SECONDARY_MODEL_PROVIDER = "google"

VERSION="v2 - model retries and timeout"

MODEL_MAP={
    "huggingface":"Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
    "google":"gemini-3.1-flash-lite-preview"
}

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2
MODEL_TIMEOUT = 60

LOG_LEVEL = "INFO"
allowed_log_levels=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

TEMPERATURE = 0.3
MAX_TOKENS = 800
TOP_P = 0.9

AUDIO_FILE="Recording.mp3"

USER_INPUT="I have google pixel 8 phone which is 2 years old. My contract with Operator expired and i should either pay 200 EUR to keep the phone or return it and buy new one. I have some old phone lying around but it is old and it does not support esim"

required_keys ={
    "default":
      [
        "goal",
        "constraints",
        "options",
        "pros_cons",
        "next_steps",
        "category",
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

validation_rules = {
    "constraints": (1,4),
    "options": (2,5),
    "pros": (1,5),
    "cons": (1,5),
    "next_steps": (2,6)
}


