# # Get first number from user
# while True:
#     try:
#         First_number = int(input("Enter a First_number number: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer number.")
# # Get second number from user
# while True:
#     try:
#         Second_number = int(input("Enter a Second_number number: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer number.")
# # Get operation from user
# while True:
#     op = input("Enter Operation (+, -, *, /)   :   ")
#     if op in ['+', '-', '*', '/']:
#         break
#     else:
#         print("Invalid operation. Please enter a valid operation.")
# # Perform the operation based on user input
# if op == '+':
#     result = First_number + Second_number
#     print(f"Addition : {result}")
# elif op == '-':
#     result = First_number - Second_number
#     print(f"Subtraction : {result}")
# elif op == '*':
#     result = First_number * Second_number
#     print(f"Multiplication : {result}")
# elif op == '/':
#     if Second_number != 0:
#         result = First_number / Second_number
#         print(f"Division : {result}")
#     else:
#         print("Error: Division by zero is not allowed.")
        
# =============== profession version
# user validation function
def get_integer_input(field_name):
    while True:
        try:
            return int(input(f"Enter {field_name}: "))

        except ValueError:
            print(f"Invalid {field_name}. Please enter an integer.")
            
# Get Two numbers from user
first_number = get_integer_input("First_number")
second_number = get_integer_input("Second_number")

# Get operation from user
while True:
    operation = input("Enter Operation (+, -, *, /)   :   ")
    if operation in ['+', '-', '*', '/']:
        break
    else:
       print(f"Invalid operation '{operation}'. Please enter +, -, *, or /.")
if operation == '+':
    result = first_number + second_number
    print(f"Addition : {result}")
elif operation == '-':
    result = first_number - second_number
    print(f"Subtraction : {result}")
elif operation == '*':
    result = first_number * second_number
    print(f"Multiplication : {result}")
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f"Division : {result}")
    else:
        print("Error: Division by zero is not allowed.")
