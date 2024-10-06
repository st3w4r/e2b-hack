from test_website import test_website


# Prompt for input from user
def get_user_input():
    website = input("Enter the website URL: ").strip()

    print("\nEnter your natural language test cases. Type 'done' when you finish.\n")
    test_cases = []
    while True:
        test_case = input("Test Case: ").strip()
        if test_case.lower() == "done":
            break
        test_cases.append(test_case)

    return website, test_cases


def main():
    # Get user input
    website, user_behavior = get_user_input()

    if not website:
        print("No url provided. Exiting.")
        return

    test_website(website=website, behavior=user_behavior)


if __name__ == "__main__":
    main()
