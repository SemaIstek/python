
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return "Dividing zero error!"
    return x / y

while True:
    print("Choose an action:")
    print("1. Addition   ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    secim = input("Choose (1/2/3/4/5): ")
    

    if secim == '5':
        print("Exit...")
        break
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter first number: "))

         
        print("Result:", add(num1, num2))
    elif secim == '2':
        print("Result:", sub(num1, num2))
    elif secim == '3':
        print("Result:", mul(num1, num2))
    elif secim == '4':
        print("Result:", div(num1, num2))
    else:
        print("Invalid value!Please try again.")
