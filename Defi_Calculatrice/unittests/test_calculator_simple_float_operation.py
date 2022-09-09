import unittest
from calculator.calculator import Calculator


class CalculatorSimplefloatOperationTests(unittest.TestCase):

    def test_addition_without_space(self):
        formula = '1.1+1.1'
        expected_output = 2.2
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
    
    def test_addition_two_positive(self):
        formula = '1.3 + 2.4'
        expected_output = 3.7
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_one_positive_one_negative(self):
        formula = '1.1 + -1.1'
        expected_output = 0
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_one_negative_one_positive(self):
        formula = '-1.1 + 2.2'
        expected_output = 1.1
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    def test_addition_two_negative(self):
        formula = '-1.1 - -1.3'
        expected_output = 0.2
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_two_positive(self):
        formula = '1.3 - 1.4'
        expected_output = -0.1
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_one_positive_one_negative(self):
        formula = '1.3 - -2.4'
        expected_output = 3.7
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    def test_substraction_one_negative_one_positive(self):
        formula = '-1.3 + 4.3'
        expected_output = 3
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
    
    def test_substraction_two_negative(self):
        formula = '-5.5 - -6.6'
        expected_output = 1.1
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    def test_multiplication_two_positive(self):
        formula = '2.0 * 8.2'
        expected_output = 16.4
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_one_positive_one_negative(self):
        formula = '2.4 * -90.8'
        expected_output = -217.92
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_one_negative_one_positive(self):
        formula = '-2.25*10.0'
        expected_output = -22.5
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_multiplication_two_negative(self):
        formula = '-2.2 * -45.2'
        expected_output = 99.44
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    def test_division_two_positive(self):
        formula = '10.4 / 5.2'
        expected_output = 2
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_division_one_positive_one_negative(self):
        formula = '10.4/-5.2'
        expected_output = -2
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_division_one_negative_one_positive(self):
        formula = '-8.4 / 2.1'
        expected_output = -4
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_division_two_negative(self):
        formula = '-4.4/-1.1'
        expected_output = 4
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)

    def test_division_by_zero(self):
        formula = '1.0/0.0'
        expected_output = "Erreur*"
        CalculatorSimplefloatOperationTests.verify_formula(self, formula, expected_output)
        
    @staticmethod
    def verify_formula(test_case, formula, expected_output):

        actual_output = Calculator.calculate(formula)
        message = "The calculator found {}, but expected {}.".format(actual_output, expected_output)
        test_case.assertAlmostEqual(actual_output, expected_output, 7, message)
    
#
# if __name__ == '__main__':
#     unittest.main()
