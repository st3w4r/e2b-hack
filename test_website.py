from dotenv import load_dotenv
from generate_code import generate_code
from code_exec import exec_code

load_dotenv()

llm_code = generate_code(website="google.com")

if llm_code.splitlines()[0].startswith("    "):
    llm_code_indented = llm_code
else: 
    llm_code_indented = '\n'.join(["    "+ln for ln in llm_code.splitlines()])


code = f"""import asyncio
import re
import os
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:

    chromium = playwright.chromium
    browser = await chromium.connect_over_cdp('wss://connect.browserbase.com?apiKey='+ os.environ["BROWSERBASE_API_KEY"])
    context = browser.contexts[0]
    page = context.pages[0]
    
{llm_code_indented}

    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

await main()
"""
print(code)
exec_code(code)

