from time import sleep

class Map:
    def __init__(self, map):
        self.map = map
        self.width = len(map[0]) - 1
        self.height = len(map)
        self.guard = self.findGuardCoords()
    def printMap(self, tiles = None):
        for i in range(self.height):
            for j in range(self.width):
                print('X' if [j, i] in tiles else self.map[i][j], end='')
    def get(self, x, y):
        if(x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1):
            return None
        return self.map[y][x]
    def findGuardCoords(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.get(i, j) == '^':
                    return (i, j)
        return None

dirs = [[0,-1], [1,0], [0,1], [-1,0]]

def walkGuard(map):
    currentPos = map.guard
    leftMap = False
    dir = 0
    prevTiles = [currentPos]
    while not leftMap:
        nextStep = [currentPos[0] + dirs[dir][0], currentPos[1] + dirs[dir][1]]
        nextTile = map.get(nextStep[0], nextStep[1])
        if nextTile == '#':
            dir = (dir + 1) % 4
        elif nextTile == '.' or nextTile == '^':
            if nextStep not in prevTiles:
                prevTiles.append(nextStep)
            currentPos = nextStep
        elif nextTile == None:
            leftMap = True
    return prevTiles

def loadMap():
    with open("test.txt") as f:
        return Map(f.readlines())

def partOne():
    m = loadMap()
    tiles = walkGuard(m)
    return len(tiles)

def partTwo():
    # TODO: Part two, behind by a lot so I'm rushing 1 stars for now
    m = loadMap()
    tiles = walkGuard(m)
    return 0

if __name__ == "__main__":
    p1 = partOne()
    p2 = partTwo()
    print(f'Part 1: {p1}, Part 2: {p2}')
