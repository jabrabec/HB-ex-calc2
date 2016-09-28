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
    print tokens
    break
