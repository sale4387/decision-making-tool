import torch
from transformers import pipeline

speach_to_text = pipeline(
    task="automatic-speech-recognition",
    model="openai/whisper-tiny",
    device=1
)

print(speach_to_text("Recording.mp3")["text"])