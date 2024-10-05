import os
from e2b_code_interpreter import CodeInterpreter


BROWSERBASE_API_KEY = os.getenv("BROWSERBASE_API_KEY")
BROWSERBASE_PROJECT_ID = os.getenv("BROWSERBASE_PROJECT_ID")

assert BROWSERBASE_API_KEY
assert BROWSERBASE_PROJECT_ID

code = """
import playwright

print('Hello, E2B Hack!')

print(playwright)

"""

with CodeInterpreter(template="e2b-hack", 
    env_vars={
        "BROWSERBASE_API_KEY": BROWSERBASE_API_KEY,
        "BROWSERBASE_PROJECT_ID": BROWSERBASE_PROJECT_ID,
    }) as sandbox:
    execution = sandbox.notebook.exec_cell("print('hello')")

    print(execution)