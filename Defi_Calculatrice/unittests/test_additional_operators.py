import unittest

from unittests.testing_utilities import verify_formula


class CalculatorAdditionalOperatorsTests(unittest.TestCase):

    def test_case_1(self):
        formula = '2^8'
        expected_output = 256
        verify_formula(self, formula, expected_output)

    def test_case_2(self):
        formula = 'sqrt(-1*-(4*4))'
        expected_output = 4
        verify_formula(self, formula, expected_output)

    def test_case_3(self):
        formula = '1+2^(4*2)'
        expected_output = 257
        verify_formula(self, formula, expected_output)
