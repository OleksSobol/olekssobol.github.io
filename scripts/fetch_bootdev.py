import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Get username from environment variable
USERNAME = os.environ.get("BOOTDEV_USERNAME")
if not USERNAME:
    raise ValueError("BOOTDEV_USERNAME environment variable is not set!")

URL = f"https://www.boot.dev/u/{USERNAME}"

# Fetch profile page
r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

# Scrape level and XP (update selectors if Boot.dev changes)
level = soup.select_one(".profile-level").text.strip() if soup.select_one(".profile-level") else "0"
xp_total_text = soup.select_one(".profile-xp").text.strip() if soup.select_one(".profile-xp") else "0"
xp_total = int("".join(filter(str.isdigit, xp_total_text)))

# Load old data to compute XP gained today
os.makedirs("_data", exist_ok=True)
data_file = "_data/bootdev.json"
try:
    with open(data_file) as f:
        old_data = json.load(f)
        xp_yesterday = old_data.get("xp_total", 0)
except FileNotFoundError:
    xp_yesterday = 0

xp_today = xp_total - xp_yesterday

# Save JSON
data = {
    "level": level,
    "xp_total": xp_total,
    "xp_today": xp_today,
    "last_updated": datetime.utcnow().isoformat()
}
with open(data_file, "w") as f:
    json.dump(data, f, indent=2)

# Update main page snippet
snippet = f"""<!--BOOTDEV_STATS_START-->
### Boot.dev Stats
- Level: {level}
- XP Today: {xp_today}
- Total XP: {xp_total}
<!--BOOTDEV_STATS_END-->"""

index_file = "index.md"
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
