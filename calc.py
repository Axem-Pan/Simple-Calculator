def add(x, y):
    answer = x + y
    return print(answer)

def sub(x, y):
    answer = x - y
    return print(answer)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Operations: add, sub")
op = input("Enter operation: ")
if op == "add":
    add(num1, num2)
elif op == "sub":
    sub(num1, num2)
