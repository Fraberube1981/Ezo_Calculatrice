import unittest
from unittests.testing_utilities import verify_formula


class CalculatorDoubleOperationTests(unittest.TestCase):

    def test_addition_and_addition(self):
        formula = '1 + (2 + 3)'
        expected_output = 6
        verify_formula(self, formula, expected_output)
        
    def test_addition_and_substraction(self):
        formula = '1 + -(1-3)'
        expected_output = 3
        verify_formula(self, formula, expected_output)
        
    def test_addition_and_multiplication(self):
        formula = '(-1.3+2.3) * 2'
        expected_output = 2
        verify_formula(self, formula, expected_output)
        
    def test_addition_and_division(self):
        formula = '-(-1.1 - -1.1)/-1'
        expected_output = 0
        verify_formula(self, formula, expected_output)
    
    def test_substraction_and_addition(self):
        formula = '1 - (1 + 5)'
        expected_output = -5
        verify_formula(self, formula, expected_output)
    
    def test_substraction_and_substraction(self):
        formula = '(1 - -2)--9.3'
        expected_output = 12.3
        verify_formula(self, formula, expected_output)
        
    def test_substraction_and_multiplication(self):
        formula = '-(1 + 4)*-3'
        expected_output = 15
        verify_formula(self, formula, expected_output)
    
    def test_substraction_and_division(self):
        formula = '(-5 - -6)/2'
        expected_output = 0.5
        verify_formula(self, formula, expected_output)
        
    def test_multiplication_and_addition(self):
        formula = '2 * (8 + 3)'
        expected_output = 22
        verify_formula(self, formula, expected_output)

    def test_multiplication_and_substraction(self):
        formula = '2 * -(90 --90)'
        expected_output = -360
        verify_formula(self, formula, expected_output)

    def test_multiplication_and_multiplication(self):
        formula = '-2*(10*-2)'
        expected_output = 40
        verify_formula(self, formula, expected_output)

    def test_multiplication_and_division(self):
        formula = '-2 * (-45/2)'
        expected_output = 45
        verify_formula(self, formula, expected_output)
        
    def test_division_and_addition(self):
        formula = '10 / (5+ 5)'
        expected_output = 1
        verify_formula(self, formula, expected_output)

    def test_division_and_substraction(self):
        formula = '10/-(5.3 -3.3)'
        expected_output = -5
        verify_formula(self, formula, expected_output)

    def test_division_and_multiplication(self):
        formula = '-10 / (2 *-2)'
        expected_output = 2.5
        verify_formula(self, formula, expected_output)

    def test_division_and_division(self):
        formula = '-10/(-2/5)'
        expected_output = 25
        verify_formula(self, formula, expected_output)

    def test_addition_and_division_by_zero(self):
        formula = '1 / (1/0)'
        expected_output = "Erreur*"
        verify_formula(self, formula, expected_output)
