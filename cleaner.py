
def clean_response(raw_response):
    if not raw_response:
        return False, None
    raw_response= raw_response.replace("```json","").replace("```","")
    start = raw_response.find("{")
    end = raw_response.rfind("}")
    if start == -1 or end == -1: 
        return False, None

    json_text = raw_response[start:end+1]

    return True, json_text