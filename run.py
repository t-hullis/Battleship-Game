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
            print(label, "|", "  ".join(row))
            label = label + 1

    def create_ship(self):
        '''
        this function adds the selected amount of  ships randomly to the baord
        '''
        for i in range(num_of_ship):
            self.x_row, self.y_column = random.randint(0, (board_size - 1)), random.randint(0, (board_size - 1))
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, (board_size - 1)), random.randint(0, (board_size - 1))
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    def fire_shot(self):
        '''
        Function which takes user inputs to fire shots at the battleships on the board
        '''
        while True:
            try:
                x_shot = int(input('Enter X coordinate of shot : '))
                y_shot = int(input('Enter Y coordinate of shot : '))
                print(f'Coordinate is X:{x_shot} Y:{y_shot} ')
            except ValueError:
                print('Not a number')

board_size = int(input("Please enter the size of the baord : "))
print(board_size)
num_of_ship = int(input("Please enter the amount of ships on the board : "))
print(num_of_ship)


game_board = GameBoard(board_size, num_of_ship)

game_board.print_board(board_size)

GameBoard.create_ship(game_board)

print(game_board.board)

