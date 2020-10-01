"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    
    expression = input("Write your equation here: ")
    expression_tokens = expression.split(" ")

    if expression_tokens[0] == "q":
        print("Quitting now")
        break
#variables
    operator = expression_tokens[0]
    num1 = expression_tokens[1]
        
    if len(expression_tokens) == 3:
        num2 = expression_tokens[2]

    #list of operations here:

    if operator == "+":
        answer = add(int(num1), int(num2))
    
    elif operator == "-":
        answer = subtract(int(num1), int(num2))
    
    elif operator == "*":
        answer = multiply(int(num1), int(num2))
    
    elif operator == "/":
        answer = divide(int(num1), int(num2))
    
    elif operator == "square":
        answer = square(int(num1))
    
    elif operator == "cube":
        answer = cube(int(num1))
    
    elif operator == "pow":
        answer = power(int(num1), int(num2))
    
    elif operator == "mod":
        answer = mod(int(num1), int(num2))
    
    #print the answer
    print(answer)
    