import re


class MapNode:
    def __init__(self, cur, left, right):
        self.cur = cur
        self.left = left
        self.right = right

    def left(self):
        return self.left
    
    def right(self):
        return self.right
    
def findNode(map, cur):
    for node in map:
        if node.cur == cur:
            return node
    return None

def parseInput(file_path):
    map = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        instructions = lines[0]
        for line in lines[1:]:
            vals = re.findall(r"\w+", line)
            if vals and len(vals) == 3:
                map.append(MapNode(vals[0], vals[1], vals[2]))
    return map, instructions

def main():
    file_path = "../input.txt"

    input = parseInput(file_path)
    map = input[0]
    instructions = input[1]

    x = findNode(map, "AAA")
    foundZZZ = False
    iter = 0

    while not foundZZZ:
        for i in instructions:
            if x.cur == "ZZZ":
                print("Found ZZZ", iter)
                foundZZZ = True
                break
            else:
                if i == "L":
                    iter += 1
                    print("L", x.cur, "->", x.left, iter)
                    x = findNode(map, x.left)
                elif i == "R":
                    iter += 1
                    print("R", x.cur, "->", x.right, iter)
                    x = findNode(map, x.right)



if __name__ == "__main__":
    main()                          