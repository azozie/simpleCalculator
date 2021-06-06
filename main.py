#simple calculator

def multiplication(num1, num2):
    return num1 * num2

def addition(num1,num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

value1 = int(input("Enter First number:\n"))
value2 = int(input("Enter Second number:\n"))

print("Select operation 1-Divi, 2-Multi, 3-Add, 4-Sub")
operation = int(input("Choose operation 1 or 2 or 3 or 4:\n "))

if operation == 1:
    print(value1, "/", value2, "=", divide(value1, value2))

elif operation == 2:
   print(value1, "*", value2, "=", multiplication(value1, value2))

elif operation == 3:
   print(value1, "+", value2, "=", addition(value1, value2))
elif operation == 4:
   print(value1, "-", value2, "=", subtraction(value1, value2))
else:
   print("Enter correct operation")