# Calculator

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}
def calculator():
    continuation = True
    number_1 = float(input("What's the first number?: \n"))
    for operation in operations:
        print(operation)
    while continuation == True:
        operation_symbol = input("Pick an operation:\n")
        calculation_function = operations[operation_symbol]
        number_2 = float(input("What's the next number?: \n"))
        answer = calculation_function(number_1, number_2)

        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        further_maths = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:\n").lower()
        if further_maths == 'y':
            number_1 = answer
        elif further_maths == 'n':
            continuation = False
            calculator()

calculator()