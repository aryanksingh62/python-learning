from datetime import datetime

content=input("Enter whta you learned today:")
rating=input("Enter the rating between(1-5):")
time=datetime.now().strftime("%Y-%m-%d - %I:%M %p")
sep="-"*100

with open("learning_journal.txt","a") as f:
    f.write(F"{time}\n{content}\nProductivity Rating: {rating}/5\n{sep}\n")