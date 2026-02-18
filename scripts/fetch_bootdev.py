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

    # Selectors from inspected DOM
    xp_text = page.locator("span.ml-2.text-xs").first.inner_text()
    level_text = page.locator("span.font-bold.text-white").first.inner_text()

    # Clean values
    def to_int(text):
        digits = "".join(filter(str.isdigit, text))
        return int(digits) if digits else 0

    xp_total = to_int(xp_text)
    level = to_int(level_text)

    # Load yesterday’s data
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

    # Update index.md
    snippet = f"""<!--BOOTDEV_STATS_START-->
### Boot.dev Stats
- Level: {level}
- XP Today: {xp_today}
- Total XP: {xp_total}
<!--BOOTDEV_STATS_END-->"""

    index_file = "_pages/lab-stats.md"
    if os.path.exists(index_file):
        with open(index_file) as f:
            content = f.read()
        if "<!--BOOTDEV_STATS_START-->" in content:
            start = content.index("<!--BOOTDEV_STATS_START-->")
            end = content.index("<!--BOOTDEV_STATS_END-->") + len("<!--BOOTDEV_STATS_END-->")
            content = content[:start] + snippet + content[end:]
        else:
            content += "\n" + snippet
        with open(index_file, "w") as f:
            f.write(content)
    else:
        with open(index_file, "w") as f:
            f.write(snippet)

    browser.close()
