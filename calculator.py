def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calc():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input")
        return

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(x, y))
    elif choice == '2':
        print("Result:", sub(x, y))
    elif choice == '3':
        print("Result:", mul(x, y))
    elif choice == '4':
        print("Result:", div(x, y))

calc()
