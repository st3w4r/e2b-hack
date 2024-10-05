import os
import sys
from e2b_code_interpreter import CodeInterpreter


def exec_code(code: str):
    BROWSERBASE_API_KEY = os.getenv("BROWSERBASE_API_KEY")
    BROWSERBASE_PROJECT_ID = os.getenv("BROWSERBASE_PROJECT_ID")

    assert BROWSERBASE_API_KEY
    assert BROWSERBASE_PROJECT_ID


    sandbox = CodeInterpreter(template="e2b-hack-playwright", timeout=20,
        envs={
            "BROWSERBASE_API_KEY": BROWSERBASE_API_KEY,
            "BROWSERBASE_PROJECT_ID": BROWSERBASE_PROJECT_ID,
        })

    execution = sandbox.notebook.exec_cell(code=code)
    print(execution)
    list_screenshots(sandbox=sandbox)


def list_screenshots(sandbox):
    content = sandbox._filesystem.list(".")
    for item in content:
        if ".png" in item.name:
            file_url = sandbox.download_url(item.path)
            print(file_url)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()


    llm_code = """
    res = await page.goto("https://e2b.dev/")
    await page.get_by_role("link", name="Sign In").click()
    assert res.status == 200
    await page.get_by_role("link", name="Sign up").click()
    await page.screenshot(path="signup.png")
    """

    code = f"""

import asyncio
import re
import os
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:

    chromium = playwright.chromium
    browser = await chromium.connect_over_cdp('wss://connect.browserbase.com?apiKey='+ os.environ["BROWSERBASE_API_KEY"])
    context = browser.contexts[0]
    page = context.pages[0]

    # ---------------------
    
    # INSERT TEST CODE HERE    
    {llm_code}
    
    # ---------------------
    await context.close()
    await browser.close()



async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

await main()
"""
    exec_code(code)


