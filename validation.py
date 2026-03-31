from config import required_keys, validation_rules

def validate_response_default(parsed_data):
    
    error_log_message=[]

    for key in required_keys["default"]:
        if key not in parsed_data:
            error_log_message.append(f"A key is missing from parsed data.\n")
            return False

    if not min(validation_rules["constraints"]) <= len(parsed_data["constraints"]) <= max(validation_rules["constraints"]):
             error_log_message.append(f"Number of constraints is wrong.\n")

    if not min(validation_rules["options"]) <= len(parsed_data["options"]) <= max(validation_rules["options"]):
             error_log_message.append(f"Number of options is wrong.\n")

    if not min(validation_rules["next_steps"]) <= len(parsed_data["next_steps"]) <= max(validation_rules["next_steps"]):
             error_log_message.append(f"Number of next steps is wrong.\n")

    for opt in parsed_data["pros_cons"]:
          
          pros = parsed_data["pros_cons"][opt]["pros"]
          cons = parsed_data["pros_cons"][opt]["cons"]

          if not  min(validation_rules["pros"]) <= len(pros) <= max(validation_rules["pros"]):
                error_log_message.append(f"Number of pros is wrong.")

          if not  min(validation_rules["cons"]) <= len(cons) <= max(validation_rules["cons"]):
                error_log_message.append(f"Number of cons is wrong.")

    if set(parsed_data["options"]) != set(parsed_data["pros_cons"].keys()):
          error_log_message.append(f"Option set not matching Pros and Cons keys.")

    if error_log_message:
          return [False, error_log_message]
    
    else:
          return [True, error_log_message]
    
def validate_response_partial(parsed_data):

      error_log_message=[]

      for key in parsed_data:

            if key not in required_keys["plan"]:
                  error_log_message.append(f"A key is missing from parsed data.\n")
                  return False

            if not min(validation_rules["options"]) <= len(parsed_data["options"]) <= max(validation_rules["options"]):
             error_log_message.append(f"Number of options is wrong.\n")

            if not min(validation_rules["next_steps"]) <= len(parsed_data["next_steps"]) <= max(validation_rules["next_steps"]):
             error_log_message.append(f"Number of next steps is wrong.\n")

      if error_log_message:
            return [False, error_log_message]
      
      else:
            return[True, error_log_message]
      
def validate_response_minimal(parsed_data):

      error_log_message=[]

      for key in parsed_data:

            if key not in required_keys["plan"]:
                  error_log_message.append(f"A key is missing from parsed data.\n")
                  return [False, error_log_message]

            else:
                  return[True, error_log_message]
            
def validate_test_cases(test_cases, allowed_categories):
    for test_case in test_cases:
        if "category" not in test_case:
            raise ValueError(f"Missing category in {test_case['name']}")
        if test_case["category"] not in allowed_categories:
            raise ValueError(f"Invalid category {test_case['category']} in {test_case['name']}")