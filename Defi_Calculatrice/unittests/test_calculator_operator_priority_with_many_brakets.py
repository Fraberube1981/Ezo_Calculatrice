import unittest
from calculator.calculator import Calculator


class CalculatorOperatorPriorityWithManyBracketsTests(unittest.TestCase):

    def test_case_1(self):
        formula = '2*-(1 + (2 + 3))+2'
        expected_output = -10
        CalculatorOperatorPriorityWithManyBracketsTests.verify_formula(self, formula, expected_output)

    def test_case_2(self):
        formula = '2*-(10 / (-2 + 7))'
        expected_output = -4
        CalculatorOperatorPriorityWithManyBracketsTests.verify_formula(self, formula, expected_output)

    def test_case_3(self):
        formula = '2--(2+2*5+5)'
        expected_output = 19
        CalculatorOperatorPriorityWithManyBracketsTests.verify_formula(self, formula, expected_output)
        
    @staticmethod
    def verify_formula(test_case, formula, expected_output):

        actual_output = Calculator.calculate(formula)
        message = "The calculator found {}, but expected {}.".format(actual_output, expected_output)
        test_case.assertAlmostEqual(actual_output, expected_output, 7, message)
    
#
# if __name__ == '__main__':
#     unittest.main()
