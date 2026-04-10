from persistence import retrieve_session

session_history=retrieve_session()

for line in session_history:
    print(line["results"]["output"])