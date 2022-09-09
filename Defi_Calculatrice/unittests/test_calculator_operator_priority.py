import unittest
from calculator.calculator import Calculator


class CalculatorDoubleOperationTests(unittest.TestCase):

    def test_addition_and_addition(self):
        formula = '1 + 2.6 + 3'
        expected_output = 6.6
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_and_substraction(self):
        formula = '1 + -1-3'
        expected_output = -3
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_and_multiplication(self):
        formula = '-1+2 * 2'
        expected_output = 3
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_and_division(self):
        formula = '-1 - -1/-1'
        expected_output = -2
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_and_addition(self):
        formula = '1 - 1 + 5'
        expected_output = 5
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_and_substraction(self):
        formula = '1 - -2.4--9.4'
        expected_output = 12.8
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_substraction_and_multiplication(self):
        formula = '-1 + 4*-3'
        expected_output = -13
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_and_division(self):
        formula = '-5 - -6/3'
        expected_output = -3
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_multiplication_and_addition(self):
        formula = '2 * 8 + 3'
        expected_output = 19
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_and_substraction(self):
        formula = '2 * -90 --90'
        expected_output = -90
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_and_multiplication(self):
        formula = '-2*10*-2'
        expected_output = 40
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_and_division(self):
        formula = '-2 * -45/2'
        expected_output = 45
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)
        
    def test_division_and_addition(self):
        formula = '10 / 5+ 5.8'
        expected_output = 7.8
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_division_and_substraction(self):
        formula = '10.4/-5.2 -2'
        expected_output = -4
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_division_and_multiplication(self):
        formula = '-10.5 / 2.1 *-2'
        expected_output = 10
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_division_and_division(self):
        formula = '-10/-2/5'
        expected_output = 1
        CalculatorDoubleOperationTests.verify_formula(self, formula, expected_output)

    def test_addition_and_division_by_zero(self):
        formula = '1 + 1/0'
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
