def user_grid_size():
    while True:
        try:
            size = int(input("Enter the grid size:"))
            if size <=0:
                print("Please enter a positive number")
            else:
                return size
        except ValueError:
            Print("Invalid input. Please enter a postive number")
grid_size = user_grid_size()            
print(size)
