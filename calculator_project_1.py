import math

def multiplication(number1:float, number2:float) -> float:
    """
    Returns the results of number1 multiplied with number2.
    """
    return number1 * number2
    
def division(number1:float, number2:float) -> float:
    """
    Returns the results of number1 divided with number2.
    """
    return number1/number2
    
def subtraction(number1:float, number2:float) -> float:
    """
    Returns the result of number1 - number2.
    """
    return number1 - number2
    
def addition(number1:float, number2:float) -> float:
    """
    Returns the result of number1 + number2.
    """
    return number1 + number2
    
def power_of(number1:float, powerOf:float) -> float:
    """
    Returns the result of number1 to the power of number2.
    """
    return number1 ** powerOf
    
def cos_calc(number1:float) -> float:
    """
    Returns the result of cos(number1).
    """
    return math.cos(number1)
    
def sin_calc(number1:float) -> float:
    """
    Returns the result of sin(number1).
    """
    return math.sin(number1)
    
def tan_calc(number1:float) -> float:
    """
    Returns the result of tan(number1).
    """
    return math.tan(number1)

def print_calculation() -> None:
    """
    This function prints the calculations depending on the numbers and operand the user has inputted.
    """
    while True:
        num1 = input("Input number 1: ")
        operand = input("Input one of the following operands (*, x, **, +, -, /, %, cos, sin, tan, ^): ")

        if operand != 'tan' or operand != 'sin' or operand != 'cos':
            num2 = input("Input number 2: ")
        else:
            num2 = -1

        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)

            if operand == '+':
                print(f'{num1} + {num2} = {addition(num1, num2)}')
                break
            elif operand == '-':
                print(f'{num1} - {num2} = {subtraction(num1, num2)}')
                break
            elif operand == '*' or operand == 'x':
                print(f'{num1} {operand} {num2} = {multiplication(num1, num2)}')
                break
            elif operand == 'cos':
                print(f'cos({num1}) = {cos_calc(num1)}')
                break
            elif operand == 'sin':
                print(f'sin({num1}) = {sin_calc(num1)}')
                break
            elif operand == 'tan':
                print(f'tan({num1}) = {tan_calc(num1)}')
                break
            elif operand == '/' or operand == '%':
                print(f'{num1} {operand} {num2} = {division(num1, num2)}')
                break
            elif operand == '^' or operand == '**':
                print(f'{num1} {operand} {num2} = {power_of(num1, num2)}')
                break
            else:
                print("Invalid Operand")
        else:
            print(f'Invalid Number')

def main() -> None:
    print_calculation()

if __name__ == "__main__":
    main()