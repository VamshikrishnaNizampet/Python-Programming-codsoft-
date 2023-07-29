def calculator():
    print("welcome to simple calculator")
    number1=float(input("enter the first number:"))
    number2=float(input("enter the second number:"))
    print("operations:")
    print("1: Addition")
    print("2: subtraction")
    print("3: multiplication")
    print("4: division")
   
    choice=int(input("enter your operation choice(1-4):"))
    
    if choice==1:
        result=number1+number2
    elif choice==2:
        result=number1-number2
    elif choice==3:
        result=number1*number2
    elif choice==4:
        result=number1/number2
    else:
        print("invalid choice")
        return
    print("Result:",result)
calculator()
    