from persistence import retrieve_session

session_history=retrieve_session()

print("last 5 lines:")
for line in session_history:
    print(f"Id: {line["id"]} - Timestamp:{line["timestamp"]}\n")