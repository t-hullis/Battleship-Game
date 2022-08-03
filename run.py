import random

board_size = int(input("Please enter the size of the baord : "))
print(board_size)
num_of_ships = int(input("Please enter the amount of ships on the board : "))
print(num_of_ships)


class GameBoard:
    '''
    Class for the game board
    '''
    def __init__(self, board_size, num_of_ships):
        self.board_size = board_size
        self.num_of_ships = num_of_ships
        self.board = [["~" for x in range(board_size)] for y in range(board_size)]

    def print_board(self):
        print([" ".join(i) for i in range(board_size)])
        for row in self.board:
            print("  ".join(row))


game_board = GameBoard(board_size, num_of_ships)
game_board.print_board()