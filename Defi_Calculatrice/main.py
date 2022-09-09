
from calculator.calculator import Calculator

if __name__ == "__main__":

    formula = "2^8*5-1"
    output = Calculator.calculate(formula)
    print("The answer is : {}".format(output))


