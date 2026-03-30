students = {}

while True:
    name=input("Enter the student name: ").lower()
    if name == "done":
        break
    else:
        if name in students:
            print("Student already exists!")
            continue
        try:
            mark = float(input(f"Enter the {name} mark: "))
            students[name] = mark
        except ValueError:
            print("enter the valid mark")
if not students:
    print(" No stundent data")
else:
    names = students.keys()
    marks= students.values()

    highest_mark = max(marks)
    lowest_mark = min(marks)

    topper=[name for name in names if students[name]==highest_mark]
    looser=[name for name in names if students[name]==lowest_mark]

    print("Total students:", len(students))
    print("Average marks:", sum(marks) / len(students))
    print(f"Highest mark is {highest_mark} score by {", ".join(topper)}")
    print(f"Lowest mark is {lowest_mark} score by {", ".join(looser)}")