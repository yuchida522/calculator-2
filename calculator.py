"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    
    expression = input("Write your equation here: ")
    expression_tokens = expression.split(" ")

#variables
    operator = expression_tokens[0]
    num1 = expression_tokens[1]
    num2 = expression_tokens[2]

    #list of operations here:
    if operator == "+":
        answer = add(int(num1), int(num2))
    
    print(answer)
    