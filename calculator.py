"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    user_input = user_input.rstrip()
    tokens = user_input.split(" ")
    tokens[1] = int(tokens[1])
    tokens[2] = int(tokens[2])
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
        print add(tokens[1], tokens[2])
    elif tokens[0] == "-":
        print subtract(tokens[1], tokens[2])
    elif tokens[0] == "*":
        print multiply(tokens[1], tokens[2])
    elif tokens[0] == "/":
        print ("%.6f" % divide(tokens[1], tokens[2]))
    # print tokens
