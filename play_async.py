import asyncio
import re
import os
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:

    chromium = playwright.chromium
    browser = await chromium.connect_over_cdp('wss://connect.browserbase.com?apiKey='+ os.environ["BROWSERBASE_API_KEY"])
    context = browser.contexts[0]
    page = context.pages[0]



    # chromium = playwright.chromium
    # browser = chromium.connect_over_cdp('wss://connect.browserbase.com?apiKey='+ os.environ["BROWSERBASE_API_KEY"])
    # context = browser.contexts[0]
    # page = context.pages[0]


    res = await page.goto("https://e2b.dev/")
    await page.get_by_role("link", name="Sign In").click()
    

    print("url:", page.url)
    print("status:", res.status)
    assert res.status == 200
    

    

    # await page.get_by_placeholder("Your email address").click()
    # await page.get_by_placeholder("Your email address").fill("zhankuatuly1@gmail.com")
    # await page.get_by_placeholder("Your password").click()
    # await page.get_by_placeholder("Your password").fill("Arsenkaz2005!")
    # await page.get_by_role("button", name="Sign in", exact=True).click()
    # await page.get_by_role("link", name="Home").click()

    # ---------------------
    await context.close()
    await browser.close()



async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

await main()