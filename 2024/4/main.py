dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

class WordSearchGrid:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])-1
        self.height = len(grid)
    def get(self, x, y):
        if(x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1):
            return None
        return self.grid[y][x]
    def countWord(self, word):
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.get(i, j) == word[0]:
                    count += self.countWordAt(word, i, j)
        return count
    def countWordAt(self, word, x, y):
        count = 0
        for d in dirs:
            for i in range(len(word)):
                x1, y1 = x + d[0] * i, y + d[1] * i
                if self.get(x1, y1) != word[i]:
                    break
                if i == len(word) - 1:
                    count += 1
        return count
    def findXMAS(self):
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                XMAS = []
                if self.get(i, j) == 'A':
                    XMAS.append(self.get(i-1, j-1))
                    XMAS.append(self.get(i+1, j-1))
                    XMAS.append(self.get(i-1, j+1))
                    XMAS.append(self.get(i+1, j+1))
                    if XMAS.count('M') == 2 and XMAS.count('S') == 2 and XMAS[0] != XMAS[3] and XMAS[1] != XMAS[2]:
                        count += 1
        return count

def load_wordsearch():
    with open('input.txt', 'r') as f:
        return WordSearchGrid(f.readlines())

def p1():
    wordsearch = load_wordsearch()
    return wordsearch.countWord('XMAS')

def p2():
    wordsearch = load_wordsearch()
    return wordsearch.findXMAS()


if __name__ == "__main__":
    partOne = p1()
    partTwo = p2()
    print(f'Part 1: {partOne}, Part 2: {partTwo}')