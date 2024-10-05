import openai
import os
from pydantic import BaseModel
import json

def generate_code():
    client = openai.OpenAI(
        base_url="https://api.fireworks.ai/inference/v1",
        api_key=os.getenv("FIREWORKS_API_KEY"),
    )

    class Result(BaseModel):
        python_code: str

    user_prompt = """Generate some simple python code that tests print(). 
Output JSON with schema { python_code: string \\\\ Python code without backticks  }."""

    chat_completion = client.chat.completions.create(
        model=os.getenv("LLM_MODEL") if os.getenv("LLM_MODEL") else "accounts/fireworks/models/mixtral-8x7b-instruct",
        response_format={"type": "json_object", "schema": Result.model_json_schema()},
        messages=[
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )


    # print(repr(chat_completion.choices[0].message.content))

    result = Result(**json.loads(chat_completion.choices[0].message.content))
    print(result.python_code)
    return result.python_code

if __name__ == '__main__':
  from dotenv import load_dotenv
  load_dotenv()
  generate_code()