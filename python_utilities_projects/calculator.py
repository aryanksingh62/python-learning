# calulator
num1=float(input("enter no.1:"))
num2=float(input("enter no.2:"))
op=input("enter operator(+,-,*,/)")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("error")
elif op=="*":
    print(num1*num2)
else:
    print("operator is not valid")