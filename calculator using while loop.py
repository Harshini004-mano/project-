def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("== Simple Calculator ==")
print("Press 'q' to quit.\n")

while True:
    op = input("Enter operation (+, -, *, / or q to quit): ")
    
    if op == "q":
        print("\nExiting... Goodbye!\n")
        break
    
    if op not in ('+', '-', '*', '/'):
        print("Invalid operation, try again.")
        continue
    
    try:
        a = float(input("Enter first value: "))
        b = float(input("Enter second value: "))
    except ValueError:
        print("Invalid number, try again.")
        continue

    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", sub(a, b))
    elif op == "*":
        print("Result:", mul(a, b))
    elif op == "/":
        print("Result:", div(a, b))
    else :
        print("invalid")