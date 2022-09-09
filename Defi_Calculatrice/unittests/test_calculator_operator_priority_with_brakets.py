import unittest
from calculator.calculator import Calculator


class CalculatorDoubleOperationTests(unittest.TestCase):

    def test_addition_and_addition(self):
        formula = '1 + (2 + 3)'
        expected_output = 6
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_and_substraction(self):
        formula = '1 + -(1-3)'
        expected_output = 3
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_and_multiplication(self):
        formula = '(-1.3+2.3) * 2'
        expected_output = 2
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_and_division(self):
        formula = '-(-1.1 - -1.1)/-1'
        expected_output = 0
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_and_addition(self):
        formula = '1 - (1 + 5)'
        expected_output = -5
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_and_substraction(self):
        formula = '(1 - -2)--9.3'
        expected_output = 12.3
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_substraction_and_multiplication(self):
        formula = '-(1 + 4)*-3'
        expected_output = 15
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_and_division(self):
        formula = '(-5 - -6)/2'
        expected_output = 0.5
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_multiplication_and_addition(self):
        formula = '2 * (8 + 3)'
        expected_output = 22
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_and_substraction(self):
        formula = '2 * -(90 --90)'
        expected_output = -360
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_and_multiplication(self):
        formula = '-2*(10*-2)'
        expected_output = 40
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_and_division(self):
        formula = '-2 * (-45/2)'
        expected_output = 45
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_division_and_addition(self):
        formula = '10 / (5+ 5)'
        expected_output = 1
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_division_and_substraction(self):
        formula = '10/-(5.3 -3.3)'
        expected_output = -5
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_division_and_multiplication(self):
        formula = '-10 / (2 *-2)'
        expected_output = 2.5
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_division_and_division(self):
        formula = '-10/(-2/5)'
        expected_output = 25
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_addition_and_division_by_zero(self):
        formula = '1 / (1/0)'
        expected_output = "Erreur*"
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    @staticmethod
    def verify_formula(test_case, formula, expected_output):

        actual_output = Calculator.calculate(formula)
        message = "The calculator found {}, but expected {}.".format(actual_output, expected_output)
        test_case.assertAlmostEqual(actual_output, expected_output, 7, message)
    
#
# if __name__ == '__main__':
#     unittest.main()
