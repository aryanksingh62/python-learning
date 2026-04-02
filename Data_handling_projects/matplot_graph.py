import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "weather_logs.csv"

def visualize_weather():
    dates= []
    temps= []
    conditions= defaultdict(int)

    with open(FILENAME,"r",encoding="utf-8") as f:
        reader= csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] +=1
            except:
                continue
    if not dates:
        print("No data is available")
        return
    
    plt.figure(figsize=(10,7))
    plt.plot(dates,temps,marker="o")
    plt.title("TEmperature over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.grid(True)
    
    plt.figure(figsize=(7,5))
    plt.bar(conditions.keys(),conditions.values(),color="skyblue")
    plt.xlabel("condition")
    plt.ylabel("Days")
    plt.show()

visualize_weather()