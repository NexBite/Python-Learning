# # user validation function
# while True:
#     comparison_operator = input("Enter Comparison Operator: ")

#     if comparison_operator in ['==', '!=', '<=', '>=', '<', '>']:
#         break

#     print("Invalid operator.")
# # Get Two numbers from user
# first_number = int(input("Enter First Number: "))
# second_number = int(input("Enter Second Number: "))

# # Get comparison operator from user
# if comparison_operator == "==":
    

# elif comparison_operator == "!=":
    

# elif comparison_operator == ">":
    

# elif comparison_operator == "<":
    

# elif comparison_operator == ">=":
    

# elif comparison_operator == "<=":
   

# print(f"{first_number} {comparison_operator} {second_number} = {result}")

import operator

# ------------------------
# Constants
# ------------------------

OPERATORS = {
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    ">": operator.gt,
    "<=": operator.le,
    ">=": operator.ge,
}

# ------------------------
# Helper Functions
# ------------------------

def get_integer_input(field_name):
    while True:
        try:
            return int(input(f"Enter {field_name}: "))
        except ValueError:
            print(f"Invalid {field_name}. Please enter an integer.")

# ------------------------
# Main Program
# ------------------------

while True:
    comparison_operator = input("Enter comparison operator: ")

    if comparison_operator in OPERATORS:
        break

    print("Invalid operator.")

first_number = get_integer_input("first number")
second_number = get_integer_input("second number")

result = OPERATORS[comparison_operator](first_number, second_number)

print(f"{first_number} {comparison_operator} {second_number} = {result}")