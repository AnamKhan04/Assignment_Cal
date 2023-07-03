def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except:
        print("Invalid value of b, Please enter valid input")

choice="yes"

while choice=="yes":

    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    opr=input("Enter operator: ")

    if opr=="+":
        print(f"The sum of {num1} and {num2} is: ",add(num1,num2))
    elif opr=="-":
        print(f"The substraction of {num1} and {num2} is: ",sub(num1,num2))
    elif opr=="*":  
        print(f"The multiplication of {num1} and {num2} is: ",mul(num1,num2))
    elif opr=="/":
        print(f"The division of {num1} and {num2} is: ",div(num1,num2))
    else:
        print("Wrong operator")
    choice=input("Enter yes to continue and no to stop: ")
