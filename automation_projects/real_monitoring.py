import psutil
import time
import os

def monitor_status():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            cpu= psutil.cpu_percent()
            ram= psutil.virtual_memory().percent
            disk= psutil.disk_usage('/').percent

            print(f"CPU: {cpu}%\nRAM: {ram}%\nDISK: {disk}%")
            if cpu>=80 or ram >=80:
                print("⚠️WARNING cpu or ram usasge is more than 80%")

            time.sleep(3)

    except KeyboardInterrupt:
        print("Monitoring stopped")

if __name__=="__main__":
    monitor_status()