from calculator.calculator import Calculator


def verify_formula(test_case, formula, expected_output):
    actual_output = Calculator.calculate(formula)
    message = "The calculator found {}, but expected {}.".format(actual_output, expected_output)
    test_case.assertAlmostEqual(actual_output, expected_output, 7, message)