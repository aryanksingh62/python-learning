# password strength checker

import random
import string
import getpass
fail=[]
user_password=getpass.getpass("Enter your passswrod:")

if  not any(i.islower() for i in user_password):
    fail.append("lower case is missing")

if  not any(i.isupper() for i in user_password):
    fail.append("upper case letter is missing")

if  not any(i.isdigit() for i in user_password):
    fail.append("there is no digit")
if  not any(i in "!@#$%^&*" for i in user_password):
    fail.append("special character is missing")
if not len(user_password)>8:
    fail.append("passwrod lenght is short")
if len(fail)==0:
    print("your passwor is strong")
else:
    for i in fail:
        print(i)

    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    remaining = random.choices(
        string.ascii_letters + string.digits + "!@#$%^&*",
        k=4
    )

    password_list = [upper, lower, digit, special] + remaining
    random.shuffle(password_list)

    strong_password = "".join(password_list)
    print("Suggested strong password:", strong_password)
