def evaluation(failed_tests, passed_tests):
    total_failed_tests=len(failed_tests)
    total_passed_tests=len(passed_tests)
    total_tests=total_failed_tests+total_passed_tests
    print(f"Failed tests: ",failed_tests, "\n")
    print(f"Passed tests",passed_tests, "\n")
    print(f"Total tests:", total_tests)

    with open ("eval_results.log", "w") as file:
        total_tests_string = repr(total_tests)
        total_passed_tests_string=repr(total_passed_tests)
        total_failed_tests_string=repr(total_failed_tests)
        file.write("Number of total tests was:" + total_tests_string +".\n")
        file.write("Number of passed tests was:" + total_passed_tests_string +".\n")
        file.write("Number of failed tests was:" + total_failed_tests_string +".\n") 