import time
exampleGrid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def printGrid(grid):
    print("Solution")
    for i in range(9):
        print(grid[i])
        
def isPossible(posX, posY, number, grid):
    for i in range(9):
        if grid[posX][i] == number:
            return False

    for i in range(9):
        if grid[i][posY] == number:
            return False

    squareX = (posX//3) * 3
    squareY = (posY//3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if grid[squareX + i][squareY + j] == number:
                return False

    return True

def solve(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for number in range(1,10):
                    if isPossible(x,y,number, grid):
                        grid[x][y] = number
                        solve(grid)
                        grid[x][y] = 0

                return
    printGrid(grid)

    

start_time = time.time()
solve(exampleGrid)
print("--- %s seconds ---" % (time.time() - start_time))
    
