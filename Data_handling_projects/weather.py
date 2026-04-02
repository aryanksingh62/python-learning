import os
import csv
from datetime import datetime
import requests

FILENAME = "weather_logs.csv"
apikey = "get your api key"

if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="",encoding="utf-8")as f:
        writer = csv.writer(f)
        writer.writerow(["Date","City","Temperature","Condition"])

def log_weather():
    city= input("Enter your city name:")
    date= datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME,"r",newline="",encoding="utf-8")as f:
        reader= csv.DictReader(f)
        for row in reader:
            if row["Date"]== date and row["City"].lower()== city.lower():
                print(" Entry for this city and date exists")
                return
    try:
        url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
        response= requests.get(url)
        data = response.json()

        if response.status_code!= 200:
            print("API Error")
            return
        temp= data["main"]["temp"]
        condition = data["weather"][0]["main"]
        with open(FILENAME,"a",newline="",encoding="utf-8")as f:
            writer = csv.writer(f)
            writer.writerow([date,city.title(),temp,condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")

    except Exception as e:
        print("Failed to make API call")

def view_logs():
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No Entries")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")

def main():
    while True:
        print("Real Time weather logger")
        print("1. Add weather log")
        print("2. View log")
        print("3. Exit")

        choice= input("choose an opion: ").strip()
        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case "3": break
            case _: print("Invalid choice")

if __name__=="__main__":
    main()