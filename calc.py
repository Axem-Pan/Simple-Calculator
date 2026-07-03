def add(x, y):
    answer = x + y
    return print(answer)

def sub(x, y):
    answer = x - y
    return print(answer)

def mult(x, y):
    answer = x * y
    return print(answer)

def div(x, y):
    answer = x / y
    return print(answer)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Operations: add, sub, mult, div")
op = input("Enter operation: ")
if op == "add":
    add(num1, num2)
elif op == "sub":
    sub(num1, num2)
elif op == "mult":
    mult(num1, num2)
elif op == "div":
    div(num1, num2)
