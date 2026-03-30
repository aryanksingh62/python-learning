def calculate_minutes(age_year):

    total_days=round(age_year*365.25)
    print(f"-{total_days:,} days old")

    total_hour=round(age_year*total_days*24)
    print(f"-{total_hour:,} hours old")

    total_minutes=round(total_hour*60)
    print(f"-{total_minutes:,} minutes old")

while True:
    user_age=float(input("enter your age:"))
    try:
        print("you are approx:")
        calculate_minutes(user_age)
        again=input("would you like to try again?(y/n)").strip().lower()
        if again!="y":
            print("Good Bye")
            break
    except:
        print("please enter a valid no. four age")