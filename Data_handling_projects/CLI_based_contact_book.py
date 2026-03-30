import csv
import os
FILENAME="contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer= csv.writer(f)
        writer.writerow(["Name","Phone","Email"])

def add_contact():
    name=input("Name:").strip()
    phone=input("Phone:").strip()
    email=input("Email:").strip()

    #check for duplactes
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["Name"].lower()==name.lower():
                print("Contacts already exits")
                return
    
    with open(FILENAME,"a", newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow([name,phone,email])
        print("contact added")

def view__contacts():
    with open(FILENAME,'r',encoding="utf-8") as f:
        reader=csv.reader(f)
        rows=list(reader)
        
        if len(rows)<1:
            print("no contacts found")
            return
        
        print("Your contacts:\n")
        for row in rows[1:]:
            print(F"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to searrch: ").strip().lower()
    found = False
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(F'{row["Name"]} | {row["Phone"]}')
                found=True

        if not found:
            print('No matching contatc found')

def delete_contact():
    kept_rows=[]
    delete=False
    
    name=input("Enter the contact name you want to Delete:")
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        header=next(reader)

        for row in reader:
            if name.lower()==row[0].lower():
                delete=True
                continue
            else:
                kept_rows.append(row)
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(kept_rows)
    if delete:
        print("contact delete succesfully")
    else:
        print("no matching contact found")

def edit_contact():
    update_rows=[]
    edited=False
    
    name=input("Enter the name of contact you want to edit:").strip().lower()
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        header=next(reader)

        for row in reader:
            if name==row[0].lower():    
                print(f"Current details: Name={row[0]}, Phone={row[1]}, Email={row[2]}")

                print("What do you want to edit?")
                print("1. Name")
                print("2. Phone")
                print("3. Email")
                choice = input("Enter choice (1-3): ").strip()

                if choice == "1":
                    row[0] = input("Enter new name: ").strip()
                elif choice == "2":
                    row[1] = input("Enter new phone: ").strip()
                elif choice == "3":
                    row[2] = input("Enter new email: ").strip()
                else:
                    print("Invalid choice. No changes made.")

                edited = True
            update_rows.append(row)
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(update_rows)
    if edited:
        print("contact edit succesfully")
    else:
        print("no matching contact found")
def main():
    while True:
        print("\nContach Book")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Edit contact")
        print("6. Exit")
        choice=input("choose an option (1-6):").strip()
        if choice=="1":
            add_contact()
        elif choice=="2":
            view__contacts()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            delete_contact()
        elif choice=="5":
            edit_contact()
        elif choice=="6":
            print("Thanks for using our software")
            break
        else:
            print("Invalid choice of number")
main()