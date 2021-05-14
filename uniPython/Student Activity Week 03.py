#this code shouldn't need comments its incredibly simple.


#Functions to return the proper calculation method based on the user choice
def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x * y




print("Pick Mathematical Equation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

while True:
    response = input("Enter choice from above: ")

    if response in (1, 2, 3, 4): #why??
        num1 = int(input("Enter first number: "))# First number
        num2 = int(input("Enter second number: "))# Second number

        #Taking the numbers and printing with the function results.
        if response == 1:
            print(num1, "-", num2, "=", addition(num1, num2))
        elif response == 2:
            print(num1, "+", num2, "=", subtraction(num1, num2))
        elif response == 3:
            print(num1, "*", num2, "=", multiplication(num1, num2))
        elif response == 4:
            print(num1, "/", num2, "=", division(num1, num2))
        break
    else:
        print("Invalid Input")