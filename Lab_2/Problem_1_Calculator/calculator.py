import abc
from abc import ABC

import numpy

from Lab_2.Problem_1_Calculator_v2.AbstractCalculator import AbstractCalculator


class NotANumber(Exception):
    pass

class TestCalculator(TestCase):
    # dekorator - uzycie standardowej biblioteki do mockowania
    @patch(numpy.derivate, return_value = 'x')
    def test_should_derivate_correctly(self):
        calculator = Calculator()
        expected_output = 'x'
    # dzieki temu ta funkcja nie jest wykonywana, tylko od razu zwraca 'a'
        self.assertEqual(calculator.Derivate(),expected_output)
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
        self.assertRaise (NotANumber, calculator.Add(f,s))
        self.assertRaise (NotANumber, calculator.Add(s,f))
        self.assertRaise (NotANumber, calculator.Add(s,s))
    #todo: wyjatek, ze nie dzielimy przez zero

class Calculator(AbstractCalculator):
    def Derivate(self, function, step):
        return numpy.derivate(function, step)
    # http://stackoverflow.com/questions/9876290/how-do-i-compute-derivative-using-numpy
    # idea mockow polega na tym, ze zamiast funkcji, ktora sie bedzie wykonywala ciagle, podmieniamy funkcje, ktora jest wykonywana np. godzine na cos prostego - jedyne co nas obchodzi, to zeby ta funkcja cos zwrocila
# alt+enter na bledzie