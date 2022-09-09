import unittest

from unittests.testing_utilities import verify_formula


class CalculatorSimpleIntegersOperationTests(unittest.TestCase):
    
    def test_addition_two_positive(self):
        formula = '1 + 2'
        expected_output = 3
        verify_formula(self, formula, expected_output)
        
    def test_addition_one_positive_one_negative(self):
        formula = '1 + -1'
        expected_output = 0
        verify_formula(self, formula, expected_output)
        
    def test_addition_one_negative_one_positive(self):
        formula = '-1 + 2'
        expected_output = 1
        verify_formula(self, formula, expected_output)
        
    def test_addition_two_negative(self):
        formula = '-1 - -1'
        expected_output = 0
        verify_formula(self, formula, expected_output)
    
    def test_substraction_two_positive(self):
        formula = '1 - 1'
        expected_output = 0
        verify_formula(self, formula, expected_output)
    
    def test_substraction_one_positive_one_negative(self):
        formula = '1 - -2'
        expected_output = 3
        verify_formula(self, formula, expected_output)
        
    def test_substraction_one_negative_one_positive(self):
        formula = '-1 + 4'
        expected_output = 3
        verify_formula(self, formula, expected_output)
    
    def test_substraction_two_negative(self):
        formula = '-5 - -6'
        expected_output = 1
        verify_formula(self, formula, expected_output)
        
    def test_multiplication_two_positive(self):
        formula = '2 * 8'
        expected_output = 16
        verify_formula(self, formula, expected_output)

    def test_multiplication_one_positive_one_negative(self):
        formula = '2 * -90'
        expected_output = -180
        verify_formula(self, formula, expected_output)

    def test_multiplication_one_negative_one_positive(self):
        formula = '-2*10'
        expected_output = -20
        verify_formula(self, formula, expected_output)

    def test_multiplication_two_negative(self):
        formula = '-2 * -45'
        expected_output = 90
        verify_formula(self, formula, expected_output)
        
    def test_division_two_positive(self):
        formula = '10 / 5'
        expected_output = 2
        verify_formula(self, formula, expected_output)

    def test_division_one_positive_one_negative(self):
        formula = '10/-5'
        expected_output = -2
        verify_formula(self, formula, expected_output)

    def test_division_one_negative_one_positive(self):
        formula = '-10 / 2'
        expected_output = -5
        verify_formula(self, formula, expected_output)

    def test_division_two_negative(self):
        formula = '-10/-2'
        expected_output = 5
        verify_formula(self, formula, expected_output)

    def test_division_by_zero(self):
        formula = '1/0'
        expected_output = "Erreur*"
        verify_formula(self, formula, expected_output)
