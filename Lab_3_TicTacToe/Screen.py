import os

from click._compat import raw_input

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    should_you_play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
    if should_you_play_again == "Y":
        return True
    print("Thanks for playing!")
    return False
