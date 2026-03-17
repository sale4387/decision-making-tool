from config import client, model_name
def call_model(prompt):
        
        completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
                }
        ],)
        
        raw = completion.choices[0].message.content.strip()
        return raw
