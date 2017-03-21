# jak tworzymy validator:
import os

class AbstractValidator:
    def validate(selfself, arg):

class NotAString(Exception):
    pass

class NoSuchFile(Exception):
    pass

class InputFileValidator(AbstractValidator):
    def validate(self, arg):
        if not self._is_string(arg): #funkcja z biblioteki standardowej, sprawdza czy dwie rzeczy sa tego samego typu
            raise NotAString()  #cos jak throw w c++ - wyrzuc wyjatek
    def _is_string(self, arg):
        return isinstance(str, arg)
    def _is_file(self, arg):
        return os.path.isfile(arg)

# kazda klase tworzymy w osobnym pliku tekstowym!

# w kodzie nigdzie nie moze byc: i, x, magic numbers - czyli nie wstawiamy popp prostu liczby

# zapoznac sie z coding standard

# kazde zadanie zaczynamy od stworzenia interfejsu

# gdzie gosc pracuje