import numbers
import sys

class CalculatorError(Exception):
    """    An exeption class for Calculator    """


class Calculator:
    """
    A terrible calculator
    """
    def add(Self, a, b):
        Self._check_operand(a)
        Self._check_operand(b)
        return a+b
        # try:
        #     return a+b
        # except TypeError:
        #     raise CalculatorError()

    def substract(Self, a, b):
        return a-b

    def multiply(Self, a, b):
        return a*b

    def divide(Self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            raise CalculatorError("Can't divide by zero")
    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" was not a number')

if __name__ == '__main__':
    print("Let's calculate!")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.substract,
        calculator.multiply,
        calculator.divide
    ]
    while True:
        print("pick an operation")
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation= input("Pick an operation: ")
        if operation == 'q':
            sys.exit()
        op = int(operation)
        a= float(input("what is a? "))
        b= float(input("what is b? "))

        try:
            print("result: ",operations[op -1](a,b))
        except CalculatorError as ex:
            print(ex)
        
