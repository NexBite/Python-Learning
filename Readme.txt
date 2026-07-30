# ===================== Step 3: Install VS Code Extensions
  Required
    Python (Microsoft)
    Pylance (Microsoft)
    Jupyter (Microsoft)
  Recommended
    Black Formatter
    isort
    Python Debugger
    Error Lens
    GitLens
    Better Comments
    Rainbow CSV
# ================================ Step 4: Create a Workspace 
    Python-Learning/
    │
    ├── Day01/
    ├── Day02/
    ├── Projects/
    ├── datasets/
    ├── notes/
    └── venv/
# ====================== Step 7: Activate Virtual Environment
   * Windows PowerShell
      .\venv\Scripts\Activate.ps1
   * Command Prompt
        venv\Scripts\activate
# ================= Step 8: Upgrade pip
    python -m pip install --upgrade pip
      Check:
           pip --version
# ================= Step 9: Install Required Packages
    pip install pandas
   * Install additional libraries you'll likely use:
        pip install numpy matplotlib openpyxl xlrd jupyter
    * For data analysis, I also recommend:
      pip install seaborn scikit-learn
# =============== Step 10: Verify Installation
      * Run
        python
      * then 
        import pandas as pd
          import numpy as np

          print(pd.__version__)
          print(np.__version__)
        Exit:
          exit()
# ================ Step 11: Select Python Interpreter
    Ctrl + Shift + P
    Type:
          Python: Select Interpreter
    Choose:
          venv
# ================ Step 12: Create Your First Python File
    Create:
        hello.py
      print("Hello Python")
      Run:
          python hello.py
# ===================== Step 13: Create Your First Pandas Program
    import pandas as pd

          students = {
              "Name": ["Kamal", "Rahul", "Amit"],
              "Age": [25, 30, 28],
              "City": ["Kolkata", "Delhi", "Mumbai"]
          }

          df = pd.DataFrame(students)

          print(df)

      * Run:
          python pandas_test.py
# ======================== Step 14: Install Jupyter Support
    Create:
      practice.ipynb
    or click:
        New File → Jupyter Notebook
    Example:
            import pandas as pd

              df = pd.DataFrame({
                  "Name": ["A", "B", "C"],
                  "Marks": [80, 90, 85]
              })

              df
# ======================= Step 15: Recommended Learning Folder Structure
                  Python-Learning
              │
              ├── 01_Basics
              │   ├── variables.py
              │   ├── operators.py
              │   ├── loops.py
              │   └── functions.py
              │
              ├── 02_OOP
              │
              ├── 03_FileHandling
              │
              ├── 04_Exception
              │
              ├── 05_Pandas
              │   ├── dataframe.py
              │   ├── filtering.py
              │   ├── sorting.py
              │   ├── merge.py
              │   ├── groupby.py
              │   └── excel.py
              │
              ├── datasets
              │
              ├── projects
              │
              └── venv
# ==================== Daily Practice Plan (30 Days)
    Week 1: Python fundamentals (variables, data types, loops, functions, collections).
    Week 2: OOP, file handling, exceptions, modules.
    Week 3: NumPy and Pandas (DataFrame creation, filtering, sorting, grouping, merging, missing data).
    Week 4: Real-world datasets, mini-projects, SQL basics, and interview questions.

    Since you mentioned you're learning Python and Pandas for a job, I recommend we follow a structured roadmap. Each day I'll give you:

    One focused topic.
    Hands-on coding exercises.
    An interview question.
    A small assignment.
    A mini project every weekend.

    By the end of 30 days, you'll have both interview preparation and a portfolio of practical exercises.

# ======================================= Week 1 – Python Fundamentals (Day 1)

   Today's topics:

    Variables
    Data Types
    User Input
    Type Conversion
    Practice Questions

        1. What is a Variable?
            A variable is a named location in memory used to store data.
            name = "Kamal"
            age = 36
            salary = 45000

            print(name)
            print(age)
            print(salary)
            --
      ✅ Variable Naming Rules

          ✅ Correct
          name = "Kamal"
          student_name = "Rahul"
          age1 = 20
          _myvariable = 100
          ❌ Wrong
          1name = "ABC"     # Cannot start with a number
          student-name = "" # Hyphen is not allowed
          class = "ABC"     # Reserved keyword
# Q: What is an exception?

Answer:

An exception is an error that occurs while a program is running. If it isn't handled, the program stops. Python provides try, except, else, and finally to handle exceptions gracefully.

# ------------Tomorrow: Day 2

We'll cover:

Comparison operators (==, !=, >, <, >=, <=)
Logical operators (and, or, not)
Type conversion (int, float, str, bool)
Assignment operators (+=, -=, *=, /=)
Membership operators (in, not in)
Identity operators (is, is not)
15–20 interview questions
10 coding exercises
1 mini project
# ------ Q: Why do we use while True with try/except?
Answer:

while True keeps asking the user until valid input is received.
try executes code that might fail.
except catches the error and prevents the program from crashing.
break exits the loop once the input is valid.

This pattern is widely used in command-line applications and is something interviewers like to see because it demonstrates robust input validation.
# -------- Why did you use while True instead of if?

A strong answer would be:

"if checks the condition only once. If the user enters invalid input, the program continues or exits. while True keeps asking until valid input is received, making the program more robust and user-friendly."

Interview Perspective

If an interviewer asks:

"Explain your calculator program."

A good answer:

"I created a reusable input validation function using exception handling. It accepts field names dynamically, validates integer input, and prevents the application from crashing. The calculator validates operators and handles division-by-zero errors."

That answer shows you understand the design, not just the syntax.
# ============== Next: Day 2 — Python Functions Deep Dive

You will learn:

Function parameters
Return values
Local vs global variables
Default arguments
*args and **kwargs
Lambda functions
Function-based mini project

# git 
git remote add origin https://github.com/NexBite/Python-Learning.git
Step 9: Push Code
git branch -M main
git push -u origin main

#= Future Daily Workflow

Every day after practice:

git add .
git commit -m "Day 2 Python functions practice"
git push

# ========================================= Day 2 – Python Operators & Type Conversion (Today's Lesson)
        Topics :
                Comparison Operators
                Logical Operators
                Type Conversion
                Assignment Operators
                Membership Operators
                Identity Operators
                Interview Questions
                Coding Exercises
                Mini Project
        ---------------------------------------------------------       
        | Operator | Meaning               | Example  | Result  |
        | -------- | --------------------- | -------- | ------- |
        | `==`     | Equal                 | `5 == 5` | `True`  |
        | `!=`     | Not Equal             | `5 != 4` | `True`  |
        | `>`      | Greater Than          | `10 > 5` | `True`  |
        | `<`      | Less Than             | `2 < 1`  | `False` |
        | `>=`     | Greater Than or Equal | `5 >= 5` | `True`  |
        | `<=`     | Less Than or Equal    | `3 <= 2` | `False` |
# ------------------ Interview Question 1

Q: What is the difference between = and ==?
Answer:
= is the assignment operator. It assigns a value to a variable.
x = 10
== is the comparison operator. It checks whether two values are equal.
x == 10
returns True or False.
#-------------------Interview Question 2
Predict the output:
x = 10
y = 10
print(x == y)
Answer:
True
Because both values are equal.
********************Today's Assignment
Complete these three exercises without looking at the answers.
Exercise 1
Take two numbers from the user and print:
==
!=
>
<
>=
<=
# ============ Interview Question

Q: Why use elif instead of multiple if statements?

Answer:

if checks every condition.
elif stops checking once one condition is true.
elif is more efficient and makes it clear that only one branch should execute.

# ==========Next Topic

We'll continue with Logical Operators:

and
or
not

These operators are used constantly in interviews and real applications, especially when validating user input and writing business rules.


# ================================= Logical Operators

1. and Operator
Rule

Returns True only if all conditions are true.

Syntax
condition1 and condition2
Example 1
age = 25
salary = 50000

print(age >= 18 and salary >= 30000)

Output

True

Because:

25 >= 18  → True
50000 >= 30000 → True

True and True → True
Example 2
age = 16
salary = 50000

print(age >= 18 and salary >= 30000)

Output

False

Because:

16 >= 18 → False
50000 >= 30000 → True

False and True → False
Truth Table
A	B	A and B
True	True	True
True	False	False
False	True	False
False	False	False
Practice 1

Write a program that asks for:

Age
Salary

If:

Age ≥ 18
Salary ≥ 30000

Print

Eligible

otherwise

Not Eligible
2. or Operator
Rule

Returns True if at least one condition is true.

Example
marks = 80
sports = True

print(marks >= 90 or sports)

Output

True

Why?

marks >= 90 → False
sports → True

False or True → True
Truth Table
A	B	A or B
True	True	True
True	False	True
False	True	True
False	False	False
Practice 2

A student gets a scholarship if:

Marks ≥ 90
OR
Sports quota = Yes

Ask the user:

Enter Marks:
Sports Quota (yes/no):

Print

Scholarship Approved

or

Scholarship Rejected
3. not Operator

not reverses a Boolean value.

Example
logged_in = False

print(not logged_in)

Output

True

Because

not False = True

Another example

logged_in = True

print(not logged_in)

Output

False
Practice 3
is_admin = False

print(not is_admin)

Predict the output before running it.

Combining Operators

Real programs combine them.

Example:

age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
else:
    print("Not Eligible")
Interview Questions
Q1

What is the difference between and and or?

Answer
and requires every condition to be true.
or requires at least one condition to be true.
Q2

Predict the output.

print(True and False)

Answer

False
Q3

Predict the output.

print(True or False)

Answer

True
Q4

Predict the output.

print(not True)

Answer

False
Mini Project

Create a login checker.

Requirements:

Ask the user:

Username:
Password:

Valid credentials:

Username = admin
Password = python123

Use the and operator.

If both are correct:

Login Successful

Otherwise:

Invalid Username or Password
Assignment (Write the Code Yourself)

Complete these four programs:

Exercise 1

Eligibility checker using and.

Exercise 2

Scholarship checker using or.

Exercise 3

Experiment with not and predict the output before running.

Exercise 4

Login system using and.

Challenge Question

Without running the code, predict the output:

x = 10

print(x > 5 and x < 20)
print(x > 15 or x == 10)
print(not (x == 10))

Write your predictions first, then run the program to verify them.

Once you've completed the four exercises, paste your code here. I'll review it like an interviewer, point out any logic issues, and show you how to make it cleaner and more Pythonic.

# ------------- Interview Question
Q: What is this called?
print("Eligible" if condition else "Not Eligible")

Answer:

It is called the conditional expression or ternary operator.


def check_eligibility(age, salary)

# ===========
Next Assignment

Let's move to the or operator.

Build a Scholarship Eligibility Checker.

Requirements:

Ask for marks (integer).
Ask:
Sports Quota (yes/no):

Rules:

If marks ≥ 90 OR sports quota is "yes", print:
Scholarship Approved

Otherwise print:

Scholarship Rejected

# ---------------------------------------------
and → Both conditions must be true.
or → At least one condition must be true.
# ----------------------------------------------

#-------------------Interview Question
Q: Why did you use .strip().lower()?

A good answer:

.strip() removes leading and trailing whitespace. .lower() converts the input to lowercase, allowing inputs like "YES", "Yes", and "yes" to be treated the same. This makes user input handling more robust.

#-------------------------Next Lesson

We'll continue with the not operator. It's a short topic, but it's frequently used in authentication, permissions, feature flags, and validation logic. After that, we'll move on to assignment operators, membership operators, and identity operators to complete the operator section. Keep this pace, and you'll build a strong Python foundation.
#---------------- Week 1 – Day 2 (Part 3)
not Operator
What is not?

The not operator reverses a Boolean value.

Original	not Result
True	False
False	True

Think of it as "opposite of".

Example 1
is_logged_in = True

print(not is_logged_in)

Output

False

Explanation

is_logged_in = True

not True = False
Example 2
is_logged_in = False

print(not is_logged_in)

Output

True
Example 3
age = 15

print(not(age >= 18))

Output

True

Why?

age >= 18

15 >= 18

False

not False

True
Real Interview Example

Suppose you're building a website.

is_logged_in = False

if not is_logged_in:
    print("Please Login")

Output

Please Login

If

is_logged_in = True

nothing is printed.

This pattern is extremely common.

Practice 1

Predict the output before running.

is_admin = False

print(not is_admin)

Answer

True
Practice 2
has_license = True

if not has_license:
    print("Cannot Drive")
else:
    print("Can Drive")

Output

Can Drive
Practice 3
password = "python123"

entered_password = input("Password: ")

if not entered_password == password:
    print("Wrong Password")
else:
    print("Welcome")
Better Style

Instead of

if not entered_password == password:

write

if entered_password != password:

Both work, but != is clearer.

Interview Question 1

What is the output?

print(not True)

Answer

False
Interview Question 2
print(not False)

Answer

True
Interview Question 3

Predict the output.

x = 10

print(not(x > 5))

Answer

False

Because

x > 5

True

not True

False
Interview Question 4
is_active = False

if not is_active:
    print("Inactive")

Output

Inactive
Common Mistake

Many beginners write:

if not x == 10:

This is valid Python, but most developers prefer:

if x != 10:

Why?

Because it's easier to read.

Use not when you're negating a Boolean variable:

if not is_logged_in:

Use != when comparing values:

if password != entered_password:
Mini Project
Login Permission Checker

Requirements:

Ask the user:
Are you logged in? (yes/no):
Convert the input to lowercase.
Convert it into a Boolean variable:
is_logged_in = login_status == "yes"
Use not.

If the user is not logged in:

Please login first.

Otherwise:

Welcome to Dashboard.
Example

Input

Are you logged in? (yes/no): yes

Output

Welcome to Dashboard.

Input

Are you logged in? (yes/no): no

Output

Please login first.
Challenge (Interview Level)

Without running the code, predict the output:

is_admin = False
is_verified = True

print(not is_admin and is_verified)
Think step by step:
not False = ?

? and True = ?

Write down your prediction before running the program.

Assignment

Write two programs:

Program 1

A login checker using the not operator.

Program 2

A website access checker.

Rules:

Ask if the user has a subscription (yes/no).
Convert the answer into a Boolean.
If the user does not have a subscription, print:
Access Denied

Otherwise print:

Access Granted
Today's Interview Tip

When an interviewer asks:

"When should you use not instead of !=?"

A strong answer is:

Use not to negate a Boolean expression or Boolean variable (e.g., if not is_logged_in:).
Use != when checking whether two values are different (e.g., if password != entered_password:).

# -------------------- Mini Project
Login Permission Checker
Requirements:
Ask the user:
Are you logged in? (yes/no):
Convert the input to lowercase.
Convert it into a Boolean variable:
is_logged_in = login_status == "yes"
Use not.
If the user is not logged in:
Please login first.
Otherwise:
Welcome to Dashboard.
# ================= Interview Question

Q: What does this line do?

is_logged_in = is_logged_in_input == "yes"

Answer:

It compares the user's input with "yes".

If the input is "yes", is_logged_in becomes True.

If the input is "no", is_logged_in becomes False.

This is a concise way to convert user input into a Boolean value.

# ========================
Next Lesson

We'll move to Assignment Operators, which are used constantly in loops, counters, accumulators, and data processing.

You'll learn:

Operator	Example	Meaning
+=	x += 5	x = x + 5
-=	x -= 2	x = x - 2
*=	x *= 3	x = x * 3
/=	x /= 2	x = x / 2
%=	x %= 2	Remainder assignment
**=	x **= 2	Power assignment
//=	x //= 2	Floor division assignment

These operators appear frequently in coding interviews and real-world Python programs, especially when processing data and working with loops.


#===============1. += (Addition Assignment)
Normal Way
x = 10

x = x + 5

print(x)

Output

15
Short Way
x = 10

x += 5

print(x)

Output

15
Dry Run
x = 10

Memory

x = 10

Now

x += 5

becomes

x = x + 5
x = 15
2. -=
salary = 50000

salary -= 5000

print(salary)

Output

45000

Equivalent to

salary = salary - 5000
3. *=
quantity = 5

quantity *= 4

print(quantity)

Output

20

Equivalent

quantity = quantity * 4
4. /=
price = 200

price /= 4

print(price)

Output

50.0

Notice the result is a float.

5. %=
number = 17

number %= 5

print(number)

Output

2

Because

17 ÷ 5

Quotient = 3
Remainder = 2
6. **=
x = 4

x **= 2

print(x)

Output

16

Equivalent

x = x ** 2
7. //=
x = 17

x //= 3

print(x)

Output

5

Because

17 // 3 = 5
Summary Table
Operator	Equivalent
+=	x = x + value
-=	x = x - value
*=	x = x * value
/=	x = x / value
%=	x = x % value
**=	x = x ** value
//=	x = x // value

# ---Mini Project
Bank Balance Simulator

Start with:

balance = 10000

Then perform these operations:

Deposit ₹5000
+=
Withdraw ₹2500
-=
Add 5% interest

(Hint: interest is balance * 0.05)

Print the final balance.