import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

url = "https://www.habous.gov.ma/prieres/horaire_hijri_2.php?ville=105"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", id="horaire")
rows = table.find_all("tr")[1:]  # skip header

prayer_times = []

for row in rows:
    columns = row.find_all("td")
    if len(columns) >= 9:
        day_name = columns[-9].get_text(strip=True)            # e.g., "الجمعة"
        date = columns[-7].get_text(strip=True)                 # e.g., "2"
        fajr = columns[-6].get_text(strip=True)
        shorouk = columns[-5].get_text(strip=True)
        duhr = columns[-4].get_text(strip=True)
        asr = columns[-3].get_text(strip=True)
        maghrib = columns[-2].get_text(strip=True)
        isha = columns[-1].get_text(strip=True)

        prayer_times.append({
            "day_name": day_name,
            "date": date,
            "fajr": fajr,
            "shorouk": shorouk,
            "duhr": duhr,
            "asr": asr,
            "maghrib": maghrib,
            "isha": isha
        })

# Save to file
with open("prayer_times.json", "w", encoding="utf-8") as f:
    json.dump(prayer_times, f, ensure_ascii=False, indent=4)

print("Prayer times saved to prayer_times.json")