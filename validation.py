from config import required_keys_plan, model_instructions_plan, required_keys, min_len_constraints,max_len_constraints, min_len_options, max_len_options, min_len_next_steps, max_len_next_steps, min_len_pros,max_len_pros, min_len_cons, max_len_cons

def validate_response_default(parsed_data):
    
    error_log_message=[]

    for key in required_keys:
        if key not in parsed_data:
            error_log_message.append(f"A key is missing from parsed data.\n")

    if not min_len_constraints <= len(parsed_data["constraints"]) <= max_len_constraints:
             error_log_message.append(f"Number of constraints is wrong.\n")

    if not min_len_options <= len(parsed_data["options"]) <= max_len_options:
             error_log_message.append(f"Number of options is wrong.\n")

    if not min_len_next_steps <= len(parsed_data["next_steps"]) <= max_len_next_steps:
             error_log_message.append(f"Number of next steps is wrong.\n")

    for opt in parsed_data["pros_cons"]:
          
          pros = parsed_data["pros_cons"][opt]["pros"]
          cons = parsed_data["pros_cons"][opt]["cons"]

          if not min_len_pros <= len(pros) <= max_len_pros:
                error_log_message.append(f"Number of pros is wrong.\n")

          if not min_len_cons <= len(cons) <= max_len_cons:
                error_log_message.append(f"Number of cons is wrong.\n")

    if set(parsed_data["options"]) != set(parsed_data["pros_cons"].keys()):
          error_log_message.append(f"Option set not matching Pros and Cons keys.\n")

    if error_log_message:
          return [False, error_log_message]
    
    else:
          return [True, error_log_message]
    
def validate_responce_partial(parsed_data):

      error_log_message=[]

      for key in parsed_data:

            if key not in required_keys_plan:
                  error_log_message.append(f"A key is missing from parsed data.\n")

            if not min_len_options <= len(parsed_data["options"]) <= max_len_options:
             error_log_message.append(f"Number of options is wrong.\n")

            if not min_len_next_steps <= len(parsed_data["next_steps"]) <= max_len_next_steps:
             error_log_message.append(f"Number of next steps is wrong.\n")

      if error_log_message:
            return [False, error_log_message]
      
      else:
            return[True, error_log_message]