from Lab_3_TicTacToe.Board import Board
from Lab_3_TicTacToe.Screen import play_again

if __name__ == "__main__":

    board = Board()
    board.display()

    while True:
        board.get_x_choice()
        board.display()
        if board.check_winner("X"):
            print("X wins!")
            if play_again():
                board.reset()
                continue
            else:
                break
        if board.cells_used == 9:
            print("Oh no! It's a tie!")
            if play_again():
                continue
            else:
                break
        board.get_o_choice()
        board.display()
        if board.check_winner("O"):
            print("O wins!")
            if play_again():
                board.reset()
                continue
            else:
                break