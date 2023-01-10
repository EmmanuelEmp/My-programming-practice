#Simple calculator in python, this calculator take the 
#basic arithmetic including square root and exponential operators but it is subject to improvement
#in the future.

""" Functions is used for each of the operators 
While loop is use to loop through the value until real number is entered
Exception is used to detect invalid input

If, else and elif condition is used to check the condition of user input

By Ochogwu Emmanuel///github: EmmanuelEmp

"""
print('='*30)
import math
#function for addiction
def add(num1, num2):
    return num1 + num2

#function for subtraction
def sub(num1, num2):
    return num1 - num2

#function for multiplication
def mul(num1, num2):
    return num1 * num2

#function for division
def div(num1, num2):
    return num1 / num2

#function for finding square root
def sqrt(num):
    return math.sqrt(num)

#function for finding square
def expo(num1, num2):
    return num1 ** num2

print("Select an operation")

while True:
    operator = input('(+, *, -, /, **, sqrt ): ')
    print("=" *30)
    #check for choice of operator
    if operator in ('+', '*', '-', '/', '**', 'sqrt'):
        try:
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
            #num = float(input("Enter a number to find it's square root"))
        except ValueError:
            print("Error. not a number")
            continue
    
        if operator == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == '*':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif operator == '-':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif operator == '/':
            print(num1, "/", num2, "=", div(num1, num2))
        
        elif operator == '**':
            print(num1, "**", num2, "=", expo(num1, num2))
            
        elif operator == 'sqrt':
            num = float(input("Enter a number to find it's square root"))
            print("square root of", int(num), "=", math.sqrt(num))
            
        #check if the user want to  perform another calculation
        more_calculation = input('Want to do more calculation? (yes/no) ')
        if more_calculation == 'no':
            break
        
    else:
       print('invalid selection')
