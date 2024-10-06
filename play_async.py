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