import unittest
from calculator.calculator import Calculator


class CalculatorAdditionalOperatorsTests(unittest.TestCase):

    def test_case_1(self):
        formula = '2^8'
        expected_output = 256
        CalculatorAdditionalOperatorsTests.verify_formula(self, formula, expected_output)

    def test_case_2(self):
        formula = 'sqrt(-1*-(4*4))'
        expected_output = 4
        CalculatorAdditionalOperatorsTests.verify_formula(self, formula, expected_output)

    def test_case_3(self):
        formula = '1+2^(4*2)'
        expected_output = 257
        CalculatorAdditionalOperatorsTests.verify_formula(self, formula, expected_output)
        
    @staticmethod
    def verify_formula(test_case, formula, expected_output):

        actual_output = Calculator.calculate(formula)
        message = "The calculator found {}, but expected {}.".format(actual_output, expected_output)
        test_case.assertAlmostEqual(actual_output, expected_output, 7, message)
