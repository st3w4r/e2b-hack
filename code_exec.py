import os
import sys
from e2b_code_interpreter import CodeInterpreter


def exec_code(code: str):
    BROWSERBASE_API_KEY = os.getenv("BROWSERBASE_API_KEY")
    BROWSERBASE_PROJECT_ID = os.getenv("BROWSERBASE_PROJECT_ID")

    assert BROWSERBASE_API_KEY
    assert BROWSERBASE_PROJECT_ID


    sandbox = CodeInterpreter(template="e2b-hack", timeout=20,
        envs={
            "BROWSERBASE_API_KEY": BROWSERBASE_API_KEY,
            "BROWSERBASE_PROJECT_ID": BROWSERBASE_PROJECT_ID,
        })

    execution = sandbox.notebook.exec_cell(code=code)
    print(execution)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    with open('play_async.py', 'r') as f:
        code = f.read()

#     code = """
# import playwright
# import os

# # print('Hello, E2B Hack!')
# # print("Playwright:", playwright)
# # """
# """
    exec_code(code)


