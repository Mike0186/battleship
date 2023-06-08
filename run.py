class Board:
    """
    Main board class. Sets the board size, number of ships, 
    the players name and the board type (player or computer)
    
    """
    def __init__(self, size, num_ships, name, board_type ):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = board_type
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.guesses = []
        self.ships = []

    def print(self):
            for row in self.board:
                print("".join(row))       

def start_game():
    """
    Starts a new game. Asks the palyer to set the board size.
    """
    while True:
        size = input("Please enter the size of you battlefield:")
        if not size.isnumeric():
            print("invalid Entry. Please input a positive integer.")
            continue
        size = int(size)
        if size < 2 or size > 10:
            print("Invalid Entry. Please choose a number between 2 and 10.")
            continue
        break
    num_ships = min(size -1, 9)

    print("-" * 120)
    player_name = input("Please Enter Your Name:\n")
    print("Welcome" + " " +(player_name.title()) + " " + "to ......\n")
    print(" ********      **       ********    ********   **        ******  *****    **       **  ******    *****    ")
    print(" **    **    **  **        **          **      **        **      **       **           **  **    **       ")
    print(" **    **    **  **        **          **      **        **      **       **       **  **  **    **       ")
    print(" ********    ******        **          **      **        *****   *****    ******   **  ******    ******   ")
    print(" ********    ******        **          **      **        *****   *****    ******   **  ******    ******   ")
    print(" **    **    **  **        **          **      **        **         **    **  **   **  **            **   ")
    print(" **    **    **  **        **          **      **        **         **    **  **   **  **            **   ")
    print(" ********    **  **        **          **      *****     ******  *****    **  **   **  **        ******   ")
    print("-" * 120)

    
    print("-" * 50)

    board = Board(size, num_ships, player_name, type="player")
    

start_game()




