import pytest
from calculator import Calculator, CalculatorError

def test_add():
    # AAA When writing a test
    # Arrange
    # Act
    # Assert
    calculator = Calculator()

    result = calculator.add(2,3)

    assert result == 5

def test_add_weird_stuff():

    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two",3)

def test_add_weirder_stuff():

    calculator = Calculator()

    with pytest.raises(CalculatorError) as context:
        result = calculator.add("two", "three")

    assert str(context.value) == '"two" was not a number'
def test_substract():

    calculator = Calculator()

    result = calculator.substract(6,3)

    assert result == 3

def test_multiply():

    calculator = Calculator()

    result = calculator.multiply(6,3)

    assert result == 18

def test_divide():

    calculator = Calculator()

    result = calculator.divide(6,3)

    assert result == 2

def test_divide_by_zero():

    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(6,0)


