
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

start_game()    


"""
def user_grid_size():
    while True:
        try:
            size = int(input("Enter the grid size:"))
            if size <=0:
                print("Please enter a positive number")
            else:
                return size
        except ValueError:
            print("Invalid input. Please enter a postive number")

class board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guess = []
        self.ships =[]
print(board)

grid_size = user_grid_size()            
print(grid_size)
"""