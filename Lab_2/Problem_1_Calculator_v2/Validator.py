import abc
import os

from Lab_1.Problem_2_Word_Counter.Exceptions import NotSuchFile
from Lab_2.Problem_1_Calculator_v2.Exceptions import NotAString


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def validate(self, to_be_validated):
        '''validate the input'''

class InputFileValidator(AbstractValidator):
    def __init__(self, to_be_validated):
        self.filename = to_be_validated
    def validate(self):
        if not self._is_string(self.filename):
            raise NotAString()
        if not self._file_exist(self.filename):
            raise NotSuchFile()
    def _is_string(self):
        return isinstance(self.filename, str)
    def _file_exists(self):
        return os.path.isfile(self.filename)