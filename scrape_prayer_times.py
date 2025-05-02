import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.habous.gov.ma/prieres/horaire_hijri_2.php?ville=105"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"id": "horaire"})
rows = table.find_all("tr")[1:]  # Skip header

prayer_times = []

now = datetime.now()
year = now.year
start_month = now.month - 1 if now.day < 5 else now.month
current_month = start_month
previous_day = 0

for row in rows:
    columns = row.find_all("td")
    if len(columns) < 9:
        continue

    day = columns[-9].text.strip()
    date_str = columns[-7].text.strip()

    try:
        day_num = int(date_str)
    except ValueError:
        continue

    if previous_day and day_num < previous_day:
        current_month += 1
        if current_month > 12:
            current_month = 1
            year += 1

    previous_day = day_num

    try:
        date_iso = datetime(year, current_month, day_num).strftime("%Y-%m-%d")
    except ValueError:
        continue

    fajr = columns[-6].text.strip()
    shorouk = columns[-5].text.strip()
    duhr = columns[-4].text.strip()
    asr = columns[-3].text.strip()
    maghrib = columns[-2].text.strip()
    isha = columns[-1].text.strip()

    prayer_times.append({
        "date": date_iso,
        "day": day,
        "fajr": fajr,
        "shorouk": shorouk,
        "duhr": duhr,
        "asr": asr,
        "maghrib": maghrib,
        "isha": isha
    })

# Save to JSON
with open("prayer_times.json", "w", encoding="utf-8") as f:
    json.dump({"prayer_times": prayer_times}, f, ensure_ascii=False, indent=2)

print("Prayer times saved to prayer_times.json")