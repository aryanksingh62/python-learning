#tip bill spilter
t_bill=float(input("Enter the total amount of bill:"))
tip_perc=int(input("enyter the percentage:"))
people=int(input("enter the no. of people:"))
t_tip=(t_bill/100)*tip_perc
fin_bill= t_tip + t_bill
per_bill=fin_bill/people
print(f"so the per head amount is {round(per_bill)}") 