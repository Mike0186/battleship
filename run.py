import random


class Board:
    """
    Main board class. Sets the board size, number of ships,
    the players name and the board type(player or computer)
    """
    def __init__(self, size, num_ships, name, board_type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = board_type
        self.board = [['. ' for _ in range(size)] for _ in range(size)]
        self.guess_list = []
        self.ships = []

    def print_board(self, show_ships=False):
        for row in self.board:
            if not show_ships:
                row = ['. ' if cell != '@ ' else '. ' for cell in row]
            print("".join(row))

    def populate_board(self,):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if (row, column) in self.ships:
                    self.board[row][column] = "@ "
                else:
                    self.board[row][column] = ". "
    """ Line 32 to 48 was cited in the code insitiute battleship game video."""

    def guess(self, x, y):
        self.guess_list.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type='computer'):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player_board":
                self.board[x][y] = "@"

    def make_guess(self):
        while True:
            x = input("Pick a row between 0" + " " + str(self.size) + "\n")
            y = input("Pick a column between 0" + " " + str(self.size) + "\n")
            if not x.isnumeric() or not y.isnumeric():
                print("Enter a postive integer between 0" + " " + str(self.size))
                continue
            x = int(x)
            y = int(y)
            result = self.guess(x, y)
            if result == "Hit":
                print("You hit a ship")
            elif result == "Miss":
                print("You Missed")


def start_game():

    """Starts a new game. Asks the palyer to set the board size."""

    while True:
        size = input("Please enter the size of you battlefield:")
        if not size.isnumeric():
            print("Invalid Entry. Please input a positive integer.")
            continue
        size = int(size)
        if size < 2 or size > 11:
            print("Invalid Entry. Please choose a number between 2 and 10.")
            continue
        break
    num_ships = size - 1

    print("-" * 120)
    player_name = input("Please Enter Your Name:\n")
    print("Welcome" + " " + (player_name.title()) + " " + "to ......\n")
    print("*******   **  **** **** **   ****** ***** **     ** ****** *****")
    print("**   ** **  ** **   **  **   **     **    **        **  ** **")
    print("**   ** **  ** **   **  **   **     **    **     ** **  ** **")
    print("******* ****** **   **  **   *****  ***** ****** ** ****** ******")
    print("******* ****** **   **  **   *****  ***** ****** ** ****** ******")
    print("**   ** **  ** **   **  **   **        ** **  ** ** **         **")
    print("**   ** **  ** **   **  **   **        ** **  ** ** **         **")
    print("******* **  ** **   **  **** ****** ***** **  ** ** **     ******")
    print("-" * 80)
    print("-" * 50)

    player_board = Board(size, num_ships, 'player', board_type='player')
    for _ in range(num_ships):
        x = random.randint(0, player_board.size - 1)
        y = random.randint(0, player_board.size - 1)
        player_board.add_ship(x, y, type='player')
    player_board.populate_board()

    computer_board = Board(size, num_ships, 'computer', board_type='computer')
    for _ in range(num_ships):
        x = random.randint(0, computer_board.size - 1)
        y = random.randint(0, computer_board.size - 1)
        computer_board.add_ship(x, y, type='computer')
    computer_board.populate_board()

    print("-" * 50)
    print((player_name.title()) + " " + "here is your battlefield.\n")
    print("-" * 50)
    computer_board.print_board(show_ships=True)
    print("-" * 50)
    print("Computer here is your battlefield\n")
    print("-" * 50)
    player_board.print_board(show_ships=False)
    print("-" * 50)

    player_board.make_guess()
    
    computer_board.make_guess()
    


start_game()






