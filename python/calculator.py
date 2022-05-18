#Calculator app

#Function to add numbers
from random import choices


def add(x, y):
    return x + y

#Function to subtract numbers
def subtract(x, y):
    return x - y

#Function to multiply numbers
def multiply(x, y):
    return x * y

#Function to divide numbers
def divide(x, y):
    return x / y

#Function for modulus
def modulus(x, y):
    return x % y



print("Welcome to calculator.py, \n\nSelect an operation:")
print("\n1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")

while True:
    #Get user input
    choice = input("Enter your choice: ")
    choices = ["1", "2", "3", "4", "5"]

    #Check if user input is valid
    if choice in choices:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
    
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
            
        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
            
        break
    else:
        print("Invalid input")