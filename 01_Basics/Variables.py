Name = "kamal"
age = 36
salary = 45000

# print(Name);
# print(age);
# print(salary);

# Program 3: Print Labels

# print("Name:", Name);
# print("Age:", age);
# print("Salary:", salary);

# Program 4: Print Labels with f-string
name = "kamal"
age = 36
salary = 45000
city = "kolkata"

# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Salary: {salary}")
# print(f"City: {city}")

# ==================Program 5: Data Types
name = "kamal"  # string
age = 36  # integer
salary = 45000.50  # float
city = "kolkata"  # string
is_employed = True  # boolean
height = 5.9  # float

# print(type(name))  # <class 'str'>
# print(type(age))  # <class 'int'>
# print(type(salary))  # <class 'float'>
# print(type(city))  # <class 'str'>
# print(type(is_employed))  # <class 'bool'>

#================  Program 6: Change Variable Value
age = 36
# print ("Age before change:", age)  # Output: Age before change: 36
age = 37
# print ("Age after change:", age)  # Output: Age after change: 37
age = age + 1
# print ("Age after increment:", age)  # Output: Age after increment: 38  

# ================ Program 7: Multiple Assignment
x,y,x ,z= 10, 20, 30, 40
# print("x:", x)  # Output: x: 30
# print("y:", y)  # Output: y: 20
# print("z:", z)  # Output: z: 40

# ================= Program 8: Swap Two Variables

a = 10
b = 20
 #print("Before swapping: a =", a, "b =", b)  # Output: Before swapping: a = 10 b = 20
a, b = b, a
# print("After swapping: a =", a, "b =", b)  # Output: After swapping: a = 20 b = 10  

# ================= Program 9: Arithmetic
# a= 20
# b = 0
# print("Addition:", a + b)  # Output: Addition: 30
# print("Subtraction:", a - b)  # Output: Subtraction: -10
# print("Multiplication:", a * b)  # Output: Multiplication: 200
# print("Division:", a / b)  # Output: Division: 0.5

# ---------Solution 1: Check Before Dividing
# a = int(input("Enter first number : "))
# b = int(input("Enter second number :  "))
# if b != 0:
#     # print("Division :", a/b)
# else:
#     # print("Division by zero is not allowed.")

# ================== Solution 2: Use try and except 
# try:
#     a=int(input("Enter first number :"))
#     b=int(input("Enter second number :"))
#     print("Division :", a/b)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")

# ================= Solution 3: Handle Multiple Errors
try:
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    print("Division :", a/b)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
    