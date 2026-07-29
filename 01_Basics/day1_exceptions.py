try :
  a = int(input("Enter a number: "))
  op  = input("Enter Operation (+, -, *, /)   :   ")
  b= int(input("Enter another number: "))
  
  if op == '+':
    print("Addition :", a+b)
  elif op == '-':
    print("Subtraction :", a-b)
  elif op == '*':
    print("Multiplication :", a*b)
  elif op == '/':
    print("Division :", a/b)
  else:
    print("Invalid operation.")
except ZeroDivisionError:
  print("Division by zero is not allowed.")
  

  