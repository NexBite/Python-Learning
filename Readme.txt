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