import requests
import csv
from bs4 import BeautifulSoup

url="https://news.ycombinator.com"

FILENAME="hn_20.csv"
def fetch_data(url):
    try:
        response= requests.get(url,headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text,"html.parser")
        titles= soup.select("span.titleline > a")
        data=[]

        for i in titles[:20]:
            link= i.get("href")
            title= i.get_text(strip=True)
            data.append({"title": title, "url": link})
        return data
    
    except requests.RequestException as e:
        print(f"Failed to fetch data:\n{e}")
        return
    
def save_to_csv(data):
    if not data:
        print("Nothing to save")
        return
    
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=["title", "url"])

        writer.writeheader()
        writer.writerows(data)

        print(f"✅ Saved Hacker News to {FILENAME}")

data= fetch_data(url)
save_to_csv(data)