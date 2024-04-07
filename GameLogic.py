
_width = 0
_height = 0
_cycles = 0
_grid = None
_running = False

def initGame(gridWidth : int, gridHeight : int):
    global _width
    global _height
    global _grid
    global _cycles

    _width = gridWidth
    _height = gridHeight
    _cycles = 0
    _grid = [[0]*gridWidth for i in range(gridHeight)]

def addCell(x: int, y: int):
    global _running
    global _grid

    if _grid is None:
        return

    if 0 > x or x > _width:
        return

    if 0 > y or y > _height:
        return

    if _running :
        return

    _grid[y][x] = 1

def getGameState():
    return _grid[:]

def printGameState():
    if _grid is None:
        print("Game has not been initialized")

    index = [i for i in range(len(_grid[0]))]

    for i in range(len(_grid)):
        print(str(i) + " :   " , _grid[i])

    print("      ", *index, sep="  " )




def gameTick():
    global _cycles
    global _grid
    global _width
    global _height

    if _grid is None:
        return

    oGrid = _grid[:]

    def numOfNeighbours(x: int, y: int):
        nonlocal oGrid
        neig = 0
        for i in range(9):
            try:
                neig = neig + oGrid[y-1+int(i/3)][x+(i%3)]
            except IndexError:
                pass

        return neig

    for h in range(_height):
        for w in range(_width):
            num = numOfNeighbours(w, h)
            if oGrid[h][w]:
                if num < 2 or num > 3:
                    _grid[h][w] = 0
                continue

            if num == 3:
                _grid[h][w] = 1

    _cycles = _cycles +1
    print("\t ----End of Cycle: " + str(_cycles) + "----")
    printGameState()
    print()

    return _grid[:]

def destoryGame():
    pass

