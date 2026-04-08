import json
import time
import uuid
import logging

logger=logging.getLogger(__name__)



def save_results(test_results, mode):
    
    run_record={
        "timestamp":time.strftime("%Y-%m-%d %H:%M:%S"),
        "mode":mode,
        "results":test_results
    }

    serialized_record=json.dumps(run_record)


    with open ("test_results.jsonl", "a", encoding="utf-8") as file:
        try:
            file.write(serialized_record + "\n")
        except  Exception as e:
            logger.error(f"Persistence failed: {e}")

def save_session(session):
    session_id = str(uuid.uuid4())
    run_record={
        "id":session_id,
        "timestamp":time.strftime("%Y-%m-%d %H:%M:%S"),
        "results":session
    }
    
    serialized_record=json.dumps(run_record)

    with open ("sessions.jsonl", "a", encoding="utf-8") as file:
        try:
            file.write(serialized_record + "\n")
        except  Exception as e:
            logger.error(f"Saving session failed: {e}")

def retrieve_session():

        try:
            with open("sessions.jsonl","r", encoding="utf-8") as file:
                last_5_lines=[]
                lines=file.readlines()[-5:]
                for line in lines:
                    single_line=json.loads(line)
                    last_5_lines.append(single_line)
                return last_5_lines    
        except Exception as e:
            logger.error(f"Retrieving session failed: {e}")
            return []
    