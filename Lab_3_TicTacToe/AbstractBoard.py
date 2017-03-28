import abc

class AbstractBoard(abc.ABC):
    @abc.abstractmethod
    def print_header(self):
        pass
    def display(self):
        pass
    def is_cell_availible(self, CellNumber):
        pass
    def update_cell(self, CellNumber, Player):
        pass
    def is_right_input(self, number):
        pass
    def get_x_choice(self):
        pass
    def get_y_choice(self):
        pass
    def is_winner(self, player):
        pass
    def reset(self):
        pass