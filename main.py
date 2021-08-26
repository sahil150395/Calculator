from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    shouldContinue = True

    while shouldContinue:
        operation_symbol = input("Pick an opeartion: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calContinue = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")

        if calContinue == "y":
            num1 = answer 
        else:
            shouldContinue = False
            calculator()

calculator()
