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

    def create_ship(self, num_of_ship, board_size):
        '''
        this function adds the selected amount of  ships randomly to the baord
        '''
        for i in range(num_of_ship):
            self.x_row, self.y_column = random.randint(0, (board_size - 1)), random.randint(0, (board_size - 1))
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, (board_size - 1)), random.randint(0, (board_size - 1))
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    def fire_shot(self, hidden_board, game_board):
        '''
        Function which takes user inputs to fire shots at the battleships on
        the board
        '''
        stopgo = True
        while stopgo:
            try:
                x_shot = int(input('Enter X coordinate of shot : '))
                y_shot = int(input('Enter Y coordinate of shot : '))
                print(f'Coordinate is X,Y : {x_shot},{y_shot} ')
                stopgo = False
            except ValueError:
                print('Not a number')
            
        if hidden_board.board[x_shot][y_shot] == "X":
            print("Ship hit!")
            game_board.board[x_shot][y_shot] = "X"
        elif hidden_board.board[x_shot][y_shot] != "X":
            print("You missed!")
            hidden_board.board[x_shot][y_shot] = "O"
            game_board.board[x_shot][y_shot] = "O"
        else:
            print("All ready selected")


def start_game():
    '''
    function to collect all the needed data to set up the board as the user 
    requests
    '''
    board_size = int(input("Please enter the size of the baord : "))

    print(board_size)

    num_of_ship = int(input("Please enter the amount of ships on the board : "))

    print(num_of_ship)

    return num_of_ship, board_size


def run_game(board_size, num_of_ship):
    
    game_board = GameBoard(board_size, num_of_ship)
    hidden_board = GameBoard(board_size, num_of_ship)

    game_board.print_board(board_size)

    hidden_board.create_ship(num_of_ship, board_size)

    print(game_board.board)
    print(hidden_board.board)

    game_board.fire_shot(hidden_board, game_board)
    game_board.print_board(board_size)
    print("====" * board_size)
    hidden_board.print_board(board_size)


b_s, n_o_s = start_game()
run_game(b_s, n_o_s)
