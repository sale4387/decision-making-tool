import json
import time

def save_results(test_results, mode):
    
    run_record={
        "timestamp":time.strftime("%Y-%m-%d %H:%M:%S"),
        "mode":mode,
        "results":test_results
    }

    serialized_list=json.dumps(run_record)


    with open ("test_results.jsonl", "a", encoding="utf-8") as file:
        try:
            file.write(serialized_list + "\n")
        except  Exception as e:
            print(f"Persistence failed: {e}")

    
    