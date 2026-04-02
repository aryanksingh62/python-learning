import os
import base64
VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length= len(password)
    h_upper= any(i.isupper() for i in password)
    h_digit= any(i.isdigit() for i in password)
    h_special= any(i in "!@#$%^&*" for i in password)
    
    score= sum([length>=8, h_upper, h_digit, h_special])
    return ["Weak", "Medium", "Strong", "Very strong"][min(score,3)]

def add_credential():
    website=input("enter website name:").strip()
    username= input("enter user name:").strip()
    password= input("enter password:").strip()

    strength = password_strength(password)
    line = f"{website}||{username}||{password}"
    encoded_line= encode(line)

    with open(VAULT_FILE,"a",encoding="utf-8") as f:
        f.write(encoded_line+"\n")
    print("✅ Credential saved")
    print(f"your password strength is {strength}")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("file not found")
        return
    with open(VAULT_FILE,"r",encoding="utf-8") as f:
        for line in f:
            decoded= decode(line.strip())
            website, username, password= decoded.split("||")
            hidden_password= "*" * len(password)
            print(f"{website} | {username} | {hidden_password}")

def update_password():
    
    website_match=input("enter the webstite name for password change:").strip()
    new_password= input("Enter new password:").strip()
    update_rows=[]

    with open(VAULT_FILE,"r",encoding="utf-8")as f:
        found=False
        for line in f:
            decoded= decode(line.strip())
            website, username, password= decoded.split("||")
            if website == website_match:
                password = new_password
                found=True

            update_rows.append(f"{website}||{username}||{password}")
        if not found:
            print(f"there is no website of this name {website_match}")
            return
        
    with open(VAULT_FILE,"w",encoding="utf-8")as f:
        for row in update_rows:
            encoded= encode(row)
            f.write(encoded + "\n")
        print(f"{website_match} password is updated")

def main():
    while True:
        print("Credential Manager")
        print("1.Add credential")
        print("2.View credential")
        print("3. Update password")
        print("4.Exit")

        choice = input("Enter your choice:")
        match choice:
            case"1": add_credential()
            case"2": view_credentials()
            case"3": update_password()
            case"4": break
            case _: print("invalid choice")
if __name__=="__main__":
    main()