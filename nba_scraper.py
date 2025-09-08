import requests
from bs4 import BeautifulSoup
import json

# NBA standings page
url = "https://www.basketball-reference.com/leagues/NBA_2025_standings.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

standings_data = []

# There are two tables: Eastern and Western Conference
tables = soup.find_all("table")

for table in tables:
    conf_name = table.get("id", "").replace("_standings", "").title()
    rows = table.tbody.find_all("tr")

    for row in rows:
        team_cell = row.find("th", {"data-stat": "team_name"})
        if not team_cell:
            continue
        team = team_cell.get_text(strip=True)

        cells = row.find_all("td")
        try:
            wins = int(row.find("td", {"data-stat": "wins"}).get_text(strip=True))
            losses = int(row.find("td", {"data-stat": "losses"}).get_text(strip=True))
            win_pct = float(row.find("td", {"data-stat": "win_loss_pct"}).get_text(strip=True))
        except (AttributeError, ValueError):
            continue

        standings_data.append({
            "conference": conf_name,
            "team": team,
            "wins": wins,
            "losses": losses,
            "win_pct": win_pct
        })

# Save to JSON
with open("nba_standings.json", "w", encoding="utf-8") as f:
    json.dump(standings_data, f, indent=4, ensure_ascii=False)

print(f"Scraping complete! {len(standings_data)} teams saved to nba_standings.json")
