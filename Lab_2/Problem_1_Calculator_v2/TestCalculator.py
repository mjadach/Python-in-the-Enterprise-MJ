from unittest import TestCase
from unittest.mock import patch

import numpy

from Lab_2.Problem_1_Calculator_v2.Calculator import Calculator
from Lab_2.Problem_1_Calculator_v2.Exceptions import NotANumber, SecondNumberZero


class TestCalculator(TestCase):
    '''
    # dekorator - uzycie standardowej biblioteki do mockowania
    @patch(numpy.derivate , return_value = 'a')
    def test_should_derivate_correctly(self):
        calculator = Calculator()
        expected_output = 'a'
    # dzieki temu ta funkcja nie jest wykonywana, tylko od razu zwraca 'a'
        self.assertEqual(calculator.Derivate(),expected_output)
        # jest zle wiec komentuje
        '''
    def test_should_something_very_very_long(self):
        calculator = Calculator()
        first = 1
        second = 12.1
        expected_sum = 13.1
        self.assertAlmostEqual (calculator.Add(first,second), expected_sum)
    def test_should_raise_exception_if_input_is_not_a_number(self):
        calculator = Calculator()
        f = 'a'
        s = 15
        self.assertRaises(NotANumber, calculator.Add(f,s))
        self.assertRaises(NotANumber, calculator.Add(s,f))
        self.assertRaises(NotANumber, calculator.Add(s,s))
    def test_should_raise_exception_if_second_number_is_zero(self):
        calculator = Calculator()
        a = 1
        b = 0
        self.assertRaises(SecondNumberZero, calculator.Divide(a,b))
        self.assertRaises(SecondNumberZero, calculator.Divide(b,a))
        self.assertRaises(SecondNumberZero, calculator.Divide(b,b))
        self.assertRaises(SecondNumberZero, calculator.Divide(a,a))
