"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
expression = input("Write your equation here: ")
expression_tokens = expression.split(" ")

while True:
    for i in range(len(expression_tokens)-1):
        if expression_tokens[0] == "+":
            num1 = expression_tokens[i + 1]
            num2 = expression_tokens[i + 2]
            print(add(num1, num2))