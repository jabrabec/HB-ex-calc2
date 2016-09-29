def add(input_numbers):
    sum_value = 0
    for index in range(len(input_numbers)):
        sum_value += int(input_numbers[index])
    return sum_value


def subtract(input_numbers):
    sub_value = int(input_numbers[0])
    for index in range(1, len(input_numbers)):
        sub_value -= int(input_numbers[index])
    return sub_value


# function does not yet accept multiple inputs
# def multiply(num1, num2):
#     sub_value = int(input_numbers[0])
#     for index in range(1, len(input_numbers)):
#         sub_value -= int(input_numbers[index])
#     return sub_value


# function does not yet accept multiple inputs
# def divide(num1, num2):
#     # Need to turn at least argument to float for division to
#     # not be integer division
#     return float(num1) / float(num2) 


# function needs to integerize input
# def square(num1):
#     # Needs only one argument
#     return num1 * num1


# function needs to integerize input
# def cube(num1):
#     # Needs only one argument
#     return num1 * num1 * num1


# function does not yet accept multiple inputs
# def power(num1, num2):
#     return num1 ** num2  # ** = exponent operator


# function does not yet accept multiple inputs
# def mod(num1, num2):
#     return num1 % num2