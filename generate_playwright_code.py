import openai
import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI()

# Load environment variables from .env file (for OpenAI API key)
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Prompt for input from user
def get_user_input():
    url = input("Enter the website URL: ").strip()

    print("\nEnter your natural language test cases. Type 'done' when you finish.\n")
    test_cases = []
    while True:
        test_case = input("Test Case: ").strip()
        if test_case.lower() == 'done':
            break
        test_cases.append(test_case)
    
    return url, test_cases

# Use GPT to generate Playwright test code from test cases
def generate_playwright_code(test_cases, url):
    # System prompt explaining the role of the AI
    system_prompt = "You are an assistant that generates Playwright test code based on website URL and natural language test cases provided by the user. Your job is return only code for testing without any explanation. Return full code for testing playwright in python using test cases. It should return code like in this example:import asyncio from playwright.async_api import Playwright, async_playwright async def run(playwright: Playwright) -> None: browser = await playwright.chromium.launch(headless=False) context = await browser.new_context() page = await context.new_page() # Navigate to the website await page.goto('https://e2b.dev/') # Click on 'Sign In' await page.get_by_role('link', name='Sign In').click() # Fill in the email await page.get_by_placeholder('Your email address').click() await page.get_by_placeholder('Your email address').fill('zhankuatuly1@gmail.com') # Fill in the password await page.get_by_placeholder('Your password').click() await page.get_by_placeholder('Your password').fill('Arsenkaz2005!') # Click on the 'Sign In' button await page.get_by_role('button', name='Sign in', exact=True).click() # Wait for navigation to complete (optional, to ensure the URL has changed) await page.wait_for_load_state('networkidle') # Print the new URL print('New URL after Sign In:', page.url) # Optionally click on the 'Home' link await page.get_by_role('link', name=Home').click() # Close the browser await context.close() await browser.close() async def main() -> None: async with async_playwright() as playwright: await run(playwright) # Run the script asyncio.run(main())"

    # Construct user input from website URL and test cases
    test_case_description = "\n".join(test_cases)
    user_prompt = f"""
Generate a Python script using Playwright to automate the following test cases for the website '{url}':

{test_case_description}

Ensure to launch the browser in headless=False mode and close the browser after execution.
"""

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)


    # Access the content correctly
    return completion.choices[0].message.content

# Main function to handle input/output
def main():
    # Get user input
    url, test_cases = get_user_input()

    if not test_cases:
        print("No test cases provided. Exiting.")
        return

    # Generate Playwright code using AI
    print("\nGenerating Playwright code...")
    playwright_code = generate_playwright_code(test_cases, url)

    # Output the generated code to the terminal
    print("\nGenerated Playwright Test Code:\n")
    print(playwright_code)

if __name__ == "__main__":
    main()
