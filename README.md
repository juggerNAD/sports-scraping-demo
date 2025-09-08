<<<<<<< HEAD
# 🏀 NBA Standings Scraper (Demo Project)

## 📌 Overview
This is a **demo project** showcasing a Python web scraper that collects **NBA standings** from [Basketball Reference](https://www.basketball-reference.com/) and outputs the data in **JSON format**.  

The project demonstrates:
- Web scraping with **BeautifulSoup + Requests**  
- Converting sports stats into **structured JSON**  
- Preparing **model-ready data** for use in sports analytics or prediction systems  

---

## 🚀 Features
- Scrapes **Eastern & Western Conference standings**  
- Extracts:
  - Team name  
  - Wins  
  - Losses  
  - Win percentage  
- Saves results into a JSON file  

---

## 🛠️ Requirements
- Python 3.8+  
- Install dependencies:  
```bash
pip install requests beautifulsoup4
```

---

## ▶️ Usage
1. Clone this repository or download the files.  
2. Run the scraper:  
```bash
python nba_scraper.py
```
3. When finished, the script will generate:  
```
nba_standings.json
```

---

## 📂 Example Output
```json
[
    {
        "conference": "E",
        "team": "Boston Celtics",
        "wins": 55,
        "losses": 27,
        "win_pct": 0.671
    },
    {
        "conference": "W",
        "team": "Denver Nuggets",
        "wins": 53,
        "losses": 29,
        "win_pct": 0.646
    }
]
```

---

## 📈 Why This Matters
This scraper is a **portfolio example** of how sports data can be:
- Collected automatically  
- Transformed into structured JSON  
- Integrated into downstream **prediction models**  

It’s a lightweight but powerful demonstration of how I can support sports analytics workflows.  
=======
# sports-scraping-demo
Demo project: Web scraper for NBA standings with JSON output
>>>>>>> 5b244cfee95428daff16faca06846526a67e75fb
