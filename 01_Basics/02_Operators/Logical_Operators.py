# age = 35
# salary = 50000

# print(age > 30 and salary > 40000)  # True, both conditions are true
# print(age > 40 or salary > 60000)   # False, neither condition is true
# print(not (age < 30))               # False, the condition is false

#==================== Practice 1
# Write a program that asks for:
    # Age
    # Salary
    # If:
    # Age ≥ 18
    # Salary ≥ 30000




# user validation function
def get_integer_input(field_name):
    while True:
        try:
            return int(input(f"Enter {field_name}: "))

        except ValueError:
            print(f"Invalid {field_name}. Please enter an integer.")

# user input 
# age = get_integer_input("your age")
# salary = get_integer_input("your salary")

# Main logic

# if age >= 18 and salary >= 30000:
#     print("You are eligible ")
# else:
#     print("You are not eligible ")
    
# print("Eligible" if age >= 18 and salary >= 30000 else "Not Eligible")

#============================== Scholarship Eligibility Checker

# def check_eligibility(marks,sports_quota):
#     is_eligible = marks >= 90 or sports_quota == "yes"
#     return "Scholarship Approved" if is_eligible else "Scholarship Rejected"

# # validation for marks input
# marks = get_integer_input("your marks")
# # validation for sports quota input
# while True:
#     sports_quota = input("Do you have a sports quota? (yes/no): ").strip().lower()

#     if sports_quota in ["yes", "no"]:
#         break

#     # print("Invalid input. Please enter yes or no.")
    

# print(check_eligibility(marks, sports_quota))

# ===========Login Permission Checker
# def check_login_permission(is_logged_in):
#     return "Please login first." if not is_logged_in else "Welcome to Dashboard."


# while True:
#     is_logged_in_input = input("Are you logged in? (yes/no): ").strip().lower()

#     if is_logged_in_input in ("yes", "no"):
#         is_logged_in = is_logged_in_input == "yes"
#         break

#     print("Invalid input. Please enter yes or no.")

# print(check_login_permission(is_logged_in))

def check_login_permission(is_logged_in):
  if is_logged_in:
    return "Welcome to Dashboard."
  else:
    return "Please login first."

while True:
    is_logged_in_input = input("Are you logged in? (yes/no): ").strip().lower()

    if is_logged_in_input in ("yes", "no"):
        is_logged_in = is_logged_in_input == "yes"
        break

    print("Invalid input. Please enter yes or no.")

print(check_login_permission(is_logged_in))