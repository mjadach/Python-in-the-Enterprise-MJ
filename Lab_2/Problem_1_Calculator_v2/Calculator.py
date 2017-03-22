
from sympy import *

from Lab_2.Problem_1_Calculator_v2.AbstractCalculator import AbstractCalculator


class Calculator(AbstractCalculator):

    def Divide(self, arg1, arg2):
        # czy to tak trzeba zrobic:
        if arg2 != 0:
            return arg1/arg2

    def Add(self, arg1, arg2):
        return arg1+arg2

    def Derivate(self, function, step):
        x = Symbol(function)
        function = x ** step
        return function.diff(x)