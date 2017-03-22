import abc
from abc import ABC

class AbstractCalculator(ABC):
    @abc.abstractmethod
    def Add(self, arg1, arg2):
        pass
    @abc.abstractmethod
    def Divide(self, arg1, arg2):
        pass
    @abc.abstractmethod
    def Derivate(self, function, step):
        pass