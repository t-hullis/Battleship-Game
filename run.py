import random

board_size = int(input("Please enter the size of the baord : " ))
print(board_size)
num_of_ships = int(input("Please enter the amount of ships on the board : "))
print(num_of_ships)

class GameBoard:
    '''
    Class for the game board
    '''
    def __init__(self, board_size, num_of_ships, board):
        self.board_size = board_size
        self.num_of_ships = num_of_ships
        self.board = board

