import os

from Lab_2.Problem_1_Calculator_v2.Exceptions import NotAString


class AbstractValidator:
    def validate(self, arg):
        return 1
        #nie mam pojecia jak to obsluzyca

class InputFileValidator(AbstractValidator):
    def validate(self, arg):
        if not self._is_string(arg):
            raise NotAString()
    def _is_string(self, arg):
        return isinstance(str, arg)
    def _is_file(self, arg):
        return os.path.isfile(arg)