from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview", contents="are you gemini from google"
)
print(response.text)