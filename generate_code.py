import openai
import os
from pydantic import BaseModel
import json


def generate_code(website: str = "google.com", behavior: str = None):
    client = openai.OpenAI(
        base_url="https://api.fireworks.ai/inference/v1",
        api_key=os.getenv("FIREWORKS_API_KEY"),
    )

    class Result(BaseModel):
        python_code: str

    if not behavior:
        behavior = "The page succesfully loads with status 200."

    user_prompt = """## Instructions
Generate some simple Playwright test for the website: {website}. 
Output JSON with schema: 
{{ python_code: string \\\\ unescaped Python code without backticks }}.

Your test should check for this behavior: 
{behavior}


## Examples

### Example 1
behavior: "The page succesfully loads."
python_code:
```
res = await page.goto("https://www.twitter.com/")
assert res.status == 200
```

### Example 2
behavior: "Click on log in link."
python_code:
```
res = await page.goto("https://www.twitter.com/")
await page.get_by_role("link", name="Log in").first.click()
```

### Example 3
behavior: "Navigate to the newsletter page enter the email mike@example.com"
python_code:
```
res = await page.goto("https://news.ycombinator.com/")
await page.get_by_role('link', name='Newsletter').first.click()
await page.fill('[name="email"]', "mike@example.com")
await page.locator('[type="submit"]').first.click()
```

### Example 4
behavior: "Search baseball results"
python_code:
```
res = await page.goto("https://www.google.com/")
await page.fill('[title="Search"]', "baseball results")
await page.locator('[type="submit"]').first.click()
```


## Context

Your code will be run in a script like this:
```
import asyncio
import re
import os
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    # ---------------------
    #
    # YOUR CODE WILL BE INSERTED HERE 
    #
    # ---------------------
    await context.close()
    await browser.close()
```
""".format(
        website=website, behavior=behavior
    )

    print(user_prompt)

    model = os.getenv("FIREWORKS_MODEL") if os.getenv("FIREWORKS_MODEL") else "accounts/fireworks/models/mixtral-8x7b-instruct"
    print(f"Using model {model}")

    chat_completion = client.chat.completions.create(
        model=model,
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


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    generate_code()
