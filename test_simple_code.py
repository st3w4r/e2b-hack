from generate_code import generate_code
from code_exec import exec_code

from dotenv import load_dotenv

load_dotenv()

code = generate_code()
exec_code(code)