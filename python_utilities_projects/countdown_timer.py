import time

try:
    total_second=abs(int(input("Enter the total seconds:")))

    while total_second>0:
        min=total_second // 60
        sec=total_second % 60

        print(F"time left: {min:02}:{sec:02}",end="\r")
        time.sleep(1)
        total_second-=1
    print("00:00")
    print("time's up!")

except ValueError:
    print("user input is not integer")