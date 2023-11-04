
grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
        
        ]

def mine_sweeper(grid):
    rows = len(grid)
    cols = len(grid[0])

    new_grid = [[0 for  j in range(cols)]for i in range(rows)]

    for i in range(rows): #we could use the enumerate function here to help with looping 
        for j in range(cols): # enumerate
            if grid[i][j] == '#':
                new_grid[i][j] = '#'
            else:

                count = 0

                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if grid[x][y] == '#' :
                            count += 1

                new_grid[i][j] = str(count) 

    return new_grid           

result = mine_sweeper(grid)
print(result)