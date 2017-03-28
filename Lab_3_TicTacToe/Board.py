from click._compat import raw_input

from Lab_3_TicTacToe.AbstractBoard import AbstractBoard
import os

from Lab_3_TicTacToe.Screen import clear_screen


class Board(AbstractBoard):
    def __init__(self):
        self.cells_used = 0
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_header(self):
        print("Welcome to Tic Tac Toe!")

    def display(self):
        clear_screen()
        self.print_header()
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def is_cell_available(self, CellNumber):
        if self.cells[CellNumber] == " ":
            return True
        return False

    def update_cell(self, CellNumber, Player):
        self.cells[CellNumber] = Player

    def is_right_input(self, number):
        try:
            int(number)
            for i in range (1, 10):
                if int(number) == i:
                    return True
        except ValueError:
            return False

    def get_x_choice(self):
        x_choice = raw_input("\nX) Please choose 1 - 9. > ")
        if self.is_right_input(x_choice):
            x_choice = int(x_choice)
            if self.is_cell_available(x_choice):
                self.update_cell(x_choice,"X")
                self.cells_used += 1
            else:
                print("\nThis cell is taken. Choose empty cell.")
                self.get_x_choice()
        else:
            print("This is not a right number.)"
                  "Choose a number between 1 and 9.")
            self.get_x_choice()

    def get_o_choice(self):
        o_choice = raw_input("\nO) Please choose 1 - 9. > ")
        if self.is_right_input(o_choice):
            o_choice = int(o_choice)
            if self.is_cell_available(o_choice):
                self.update_cell(o_choice,"O")
                self.cells_used += 1
            else:
                print("\nThis cell is taken. Choose empty cell.")
                self.get_o_choice()
        else:
            print("This is not a right number.)"
                  "Choose a number between 1 and 9.")
            self.get_o_choice()

    def check_winner(self, player):
        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result == True:
                return True
        return False

    def reset(self):
        self.cells_used = 0
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]