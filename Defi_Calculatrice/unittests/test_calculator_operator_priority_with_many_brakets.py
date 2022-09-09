import unittest

from unittests.testing_utilities import verify_formula


class CalculatorOperatorPriorityWithManyBracketsTests(unittest.TestCase):

    def test_case_1(self):
        formula = '2*-(1 + (2 + 3))+2'
        expected_output = -10
        verify_formula(self, formula, expected_output)

    def test_case_2(self):
        formula = '2*-(10 / (-2 + 7))'
        expected_output = -4
        verify_formula(self, formula, expected_output)

    def test_case_3(self):
        formula = '2--(2+2*5+5)'
        expected_output = 19
        verify_formula(self, formula, expected_output)
