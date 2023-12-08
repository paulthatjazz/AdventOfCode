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
    startingNodes = []

    for node in map:
        if(node.cur.endswith("A")):
            startingNodes.append(node)

    iter = [0] * len(startingNodes)
    for x, node in enumerate(startingNodes):
        while not node.cur.endswith("Z"):
            for i in instructions:
                if i == "L":
                    iter[x] += 1
                    node = findNode(map, node.left)
                elif i == "R":
                    iter[x] += 1
                    node = findNode(map, node.right)

    for i in range(len(iter)-1):
        m = max(iter[i], iter[i+1])
        accum = m
        while (accum % iter[i] != 0 or accum % iter[i+1] != 0):
            accum += m
        iter[i+1] = accum
    
    print(iter[-1])


if __name__ == "__main__":
    main()                          