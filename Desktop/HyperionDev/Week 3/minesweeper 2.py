#grid definition
grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]       
        ]

def minesweeper(grid): #here, a function called 'minesweeper' is defined that holds 'grid'
    rows = len(grid) #this counts the number of rows in the grid and stores them in 'rows'
    cols = len(grid[0])  #counts the number of columns and stores them in 'cols'

    new_grid = [[0 for column in range(cols)]for i in range(rows)] #new grid is created on this block and it has the same characters as the main grid and is set to zero to start off with to count the number of mines around a cell

    for i, row in enumerate(grid): # enumerate function is used to simplify the rows and columns while it keeps the corresponding index
        for column, cell in enumerate(row): # enumerate function is used to simplify the rows and columns while it keeps the corresponding index
            if cell == '#': #in the loop, the iteration looks to find if the column contains the '#' character
                new_grid[i][column] = '#' #if the '#' is present in the iteration above, it is also added into the new grid
            else:
                count = 0 #here, in the case of the cell not having the '#' character, it counts the number of cells tat have the '#' character
                for x in range(max(0, i-1), min(rows, i+2)): #
                    for y in range(max(0, column-1), min(cols, column+2)): #using max function starts the iteration off at the first column and the sy=tops at the last column using the min function
                        if grid[x][y] == '#' : #checks if the grid has a mine and if it does, it counts +1
                            count += 1 #this increases the mine by one increment during each iteration
                new_grid[i][column] = str(count) #this converts the value that has been counted into a string

    return new_grid  #returns the new grid that has been iterated in the For Loop

result = minesweeper(grid) 
print(result) #prints out the resulting list which has been iterated