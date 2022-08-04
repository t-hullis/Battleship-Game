import random 


class GameBoard:
    '''
    Class for the game board
    '''
    def __init__(self, board_size, num_of_ship):
        self.board_size = board_size
        self.num_of_ship = num_of_ship
        self.board = [["~" for x in range(board_size)] for y in range(board_size)]

    def print_board(self, board_size):
        '''
        This function sets up the board for the player 
        '''
        print("  |", end=" ")
        for i in range(board_size):
            print(f"{i + 1} ", end=" ")
        print("\n--", "---" * board_size)
        label = 1
        for row in self.board:
            print(label,"|", "  ".join(row))
            label = label + 1


board_size = int(input("Please enter the size of the baord : "))
print(board_size)
num_of_ship = int(input("Please enter the amount of ships on the board : "))
print(num_of_ship)


game_board = GameBoard(board_size, num_of_ship)

game_board.print_board(board_size)

