import os
import json
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

USERNAME = os.environ.get("BOOTDEV_USERNAME")
URL = f"https://www.boot.dev/u/{USERNAME}"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")

    # Debug: save rendered HTML to see structure
    Path("debug.html").write_text(page.content())

    # Adjust selectors based on actual DOM
    # You might need to tweak these by inspecting debug.html
    level_el = page.locator("text=Level").first
    xp_el = page.locator("text=XP").first

    level_text = level_el.inner_text() if level_el.count() > 0 else "0"
    xp_text = xp_el.inner_text() if xp_el.count() > 0 else "0"

    # Clean numbers
    level = int("".join(filter(str.isdigit, level_text)))
    xp_total = int("".join(filter(str.isdigit, xp_text)))

    # Load old data
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

    browser.close()
