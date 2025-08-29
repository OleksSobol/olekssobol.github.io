import asyncio
from playwright.async_api import async_playwright
import json
import os
from datetime import datetime
from pathlib import Path

USERNAME = os.environ.get("BOOTDEV_USERNAME")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"https://www.boot.dev/u/{USERNAME}", wait_until="networkidle")

        # grab text from DOM
        level = await page.inner_text("text=Level")  # might need a tighter selector
        xp_text = await page.inner_text("text=XP")   # again, adjust selector

        # clean values
        level = int("".join(filter(str.isdigit, level)))
        xp_total = int("".join(filter(str.isdigit, xp_text)))

        # load old stats
        Path("_data").mkdir(exist_ok=True)
        data_file = Path("_data/bootdev.json")
        try:
            with open(data_file) as f:
                old = json.load(f)
                xp_yesterday = old.get("xp_total", 0)
        except FileNotFoundError:
            xp_yesterday = 0

        xp_today = xp_total - xp_yesterday

        data = {
            "level": level,
            "xp_total": xp_total,
            "xp_today": xp_today,
            "last_updated": datetime.utcnow().isoformat()
        }
        data_file.write_text(json.dumps(data, indent=2))

        await browser.close()

asyncio.run(main())
