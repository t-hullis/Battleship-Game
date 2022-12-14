import random as r

# KEY:
# b_s,        n_o_s,       p_b,          h_b_p,               c_b,
# board_size, num_of_ship, player_board, hidden_board_player, computer_board
# h_b_c
# hidden_board_computer


class GameBoard:
    '''
    Class for the game board
    '''
    def __init__(self, b_s, n_o_s):
        self.b_s = b_s
        self.n_o_s = n_o_s
        self.board = [["~" for x in range(b_s)] for y in range(b_s)]

    def print_board(self):
        '''
        This function sets up the board for the player
        '''
        print("  |", end=" ")
        for i in range(self.b_s):
            print(f"{i + 1} ", end=" ")
        print("\n--", "---" * self.b_s)
        label = 1
        for row in self.board:
            print(label, "|", "  ".join(row))
            label = label + 1

    def create_ship(self, n_o_s, b_s):
        '''
        this function adds the selected amount of  ships randomly to the baord
        '''
        for i in range(n_o_s):
            self.x_row = r.randint(0, (b_s - 1))
            self.y_column = r.randint(0, (b_s - 1))
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row = r.randint(0, (b_s - 1))
                self.y_column = r.randint(0, (b_s - 1))
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def fire_shot(self, h_b_p, p_b, b_s, c_b, h_b_c):
        '''
        Function which takes user inputs to fire shots at the battleships on
        the board
        '''
        stopgo = True
        while stopgo:
            try:
                x_shot = int(input('Enter Horizontal coordinate : ')) - 1
                while x_shot not in range(b_s):
                    print(f"Error, please enter a number between 1 and {b_s}")
                    x_shot = int(input('Enter Horizontal coordinate : ')) - 1
                y_shot = int(input('Enter Vertical coordinate : ')) - 1
                while y_shot not in range(b_s):
                    print(f"Error, please enter a number between 1 and {b_s}")
                    y_shot = int(input('Enter Vertical coordinate : ')) - 1
                stopgo = False
            except ValueError:
                print('Not a number')

        ''' Player Shot'''
        if h_b_c.board[y_shot][x_shot] == "X":
            print("You hit the computers ship!")
            c_b.board[y_shot][x_shot] = "H"
            h_b_c.board[y_shot][x_shot] = "H"
        elif h_b_c.board[y_shot][x_shot] == "H":
            print("You have already hit this ship")
        elif h_b_c.board[y_shot][x_shot] != "X":
            print("You missed!")
            h_b_c.board[y_shot][x_shot] = "O"
            c_b.board[y_shot][x_shot] = "O"
        else:
            print("All ready selected")
        ''' Computer Shot '''
        x_shot_comp = r.randint(0, (b_s - 1))
        y_shot_comp = r.randint(0, (b_s - 1))
        while (h_b_p.board[y_shot_comp][x_shot_comp] == "O" or
                h_b_p.board[y_shot_comp][x_shot_comp] == "H"):
            x_shot_comp = r.randint(0, (b_s - 1))
            y_shot_comp = r.randint(0, (b_s - 1))
        if h_b_p.board[y_shot_comp][x_shot_comp] == "X":
            print("Computer hit your hip!")
            p_b.board[y_shot_comp][x_shot_comp] = "H"
            h_b_p.board[y_shot_comp][x_shot_comp] = "H"
        elif h_b_p.board[y_shot_comp][x_shot_comp] == "H":
            print("already hit this shot")
        elif h_b_p.board[y_shot_comp][x_shot_comp] != "X":
            print("Computer missed your ships!")
            h_b_p.board[y_shot_comp][x_shot_comp] = "O"
            p_b.board[y_shot_comp][x_shot_comp] = "O"
        else:
            print("All ready selected")

    def count_hit_ships(self):
        '''
        Searches for hit ships on the boards, so a score of the game can be
        given.
        '''
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "H":
                    hit_ships += 1
        return hit_ships


def start_game():
    '''
    function to collect all the needed data to set up the board as the user
    requests
    '''
    print("Welcome to Battleships!")
    print("""
    1,  Choose the size of the board (between 3 and 15) and the number
        of battleships you would like to be placed on the board.

    2,  Guess the coordinates of the ships on the computer board.

    3,  You can see where the shots have been placed on your board,
        denoted by the X.

    4,  If you place a shot in the same place twise, you will lose
        that go, so make sure you shot to different coordinates
        each time.

    5,  The first one to find all the oppostions battleships
        wins!
    """)
    b_s = int(input("Please enter the size of the board : "))

    print(b_s)

    n_o_s = int(input("Please enter the amount of ships on the board : "))

    print(n_o_s)

    p_b = GameBoard(b_s, n_o_s)
    h_b_p = GameBoard(b_s, n_o_s)
    h_b_p.create_ship(n_o_s, b_s)

    c_b = GameBoard(b_s, n_o_s)
    h_b_c = GameBoard(b_s, n_o_s)
    h_b_c.create_ship(n_o_s, b_s)

    print("   ")
    print("   ")
    print("Your Board:")
    h_b_p.print_board()
    print("====" * b_s)
    print("Computer Board:")
    c_b.print_board()

    return b_s, n_o_s, p_b, h_b_p, c_b, h_b_c


def run_game(b_s, n_o_s, p_b, h_b_p, c_b, h_b_c):
    '''
    This is the looping function which makes each round of the game.
    '''
    game_continue = True
    game_round = 1
    while game_continue:
        print("  ")
        print("  ")
        print("===========================================")
        print(f"This is round {game_round}!")
        # The boards being printed to the user
        p_b.fire_shot(h_b_p, p_b, b_s, c_b, h_b_c)
        print("   ")
        print("Your Board:")
        h_b_p.print_board()
        print("====" * b_s)
        print("Computer Board:")
        c_b.print_board()
        game_round += 1
        print("    " * b_s)

        player_hits = h_b_c.count_hit_ships()
        computer_hits = h_b_p.count_hit_ships()
        # Scoreboard
        print(f"Player {player_hits} : {computer_hits} Computer")
        if computer_hits == n_o_s:
            print("The computer has won!")
            print("Press enter to end the game or")
            restart = input("Press r, then enter to restart: ")
            if restart == "r":
                b_sn, n_o_sn, p_bn, h_b_pn, c_bn, h_b_cn = start_game()
                run_game(b_sn, n_o_sn, p_bn, h_b_pn, c_bn, h_b_cn)
            game_continue = False
        elif player_hits == n_o_s:
            print("You have won!")
            print("Press enter to end the game or")
            restart = input("Press r, then enter to restart: ")
            if restart == "r":
                b_sn, n_o_sn, p_bn, h_b_pn, c_bn, h_b_cn = start_game()
                run_game(b_sn, n_o_sn, p_bn, h_b_pn, c_bn, h_b_cn)
            game_continue = False
        else:
            exit_game = input("Press ENTER to contiue. Press n to exit :")
            if exit_game == "n":
                game_continue = False
        

b_sn, n_o_sn, p_bn, h_b_pn, c_bn, h_b_cn = start_game()
run_game(b_sn, n_o_sn, p_bn, h_b_pn, c_bn, h_b_cn)
