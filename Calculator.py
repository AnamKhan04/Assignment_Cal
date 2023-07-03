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

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print(f"The sum of {num1} and {num2} is: ",add(num1,num2))
print(f"The substraction of {num1} and {num2} is: ",sub(num1,num2))
print(f"The multiplication of {num1} and {num2} is: ",mul(num1,num2))
print(f"The division of {num1} and {num2} is: ",div(num1,num2))