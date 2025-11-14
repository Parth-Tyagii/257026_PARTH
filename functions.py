def calculator():
    print("addition")
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    sum=num1+num2
    print(f"the sum of given numbers is",{sum})
    print("multiplication")
    mul= num1*num2
    print(f"the square of given number is",{mul})
    print("subtraction")
    sub=num1-num2
    print(f"the subtraction of given numbers is",{sub})
    print("division")
    div=num1/num2
    print(f"the division of given numbers is",{div})
calculator()