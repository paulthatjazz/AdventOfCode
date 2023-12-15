import copy

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = [0] * w * h
    def copy(self):
        return copy.deepcopy(self)
    def validateSquare(self, x, y):
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return False
        return True
    def get(self, x, y):
        if not self.validateSquare(x, y):
            return None
        return self.data[y * self.w + x]
    def set(self, x, y, value):
        if not self.validateSquare(x, y):
            print("Invalid square")
        else:
            self.data[y * self.w + x] = value
    def show(self):
        for y in range(self.h):
            print("".join([str(self.get(x, y)) for x in range(self.w)]))
    def shift(self, direction="N"):
        if direction == "N":        
            for y in range(self.h):
                for x in range(self.w):
                    tile = self.get(x, y)
                    if tile == "O":
                        ty = y
                        while True:
                            ty = ty - 1
                            upper = self.get(x, ty)
                            if upper == ".":
                                self.set(x, ty, tile)
                                self.set(x, ty+1, ".")
                            else:
                                break
        elif direction == "S":
            for y in reversed(range(self.h)):
                for x in range(self.w):
                    tile = self.get(x, y)
                    if tile == "O":
                        ty = y
                        while True:
                            ty = ty + 1
                            lower = self.get(x, ty)
                            if lower == ".":
                                self.set(x, ty, tile)
                                self.set(x, ty - 1, ".")
                            else:
                                break
        elif direction == "E":            
            for y in range(self.h):
                for x in reversed(range(self.w)):
                    tile = self.get(x, y)
                    if tile == "O":
                        tx = x
                        while True:
                            tx = tx + 1
                            upper = self.get(tx, y)
                            if upper == ".":
                                self.set(tx, y, tile)
                                self.set(tx - 1, y, ".")
                            else:
                                break
        elif direction == "W":
            for y in range(self.h):
                for x in range(self.w):
                    tile = self.get(x, y)
                    if tile == "O":
                        tx = x
                        while True:
                            tx = tx - 1
                            upper = self.get(tx, y)
                            if upper == ".":
                                self.set(tx, y, tile)
                                self.set(tx + 1, y, ".")
                            else:
                                break
        else:
            print("Invalid direction")
            return
    def shiftNtimes(self, n, pattern):
        for i in range(n):
            print("#"+str(i), self.calculateLoad())
            for p in pattern:
                self.shift(p)
    def shiftNtimesDetectCycle(self, n, pattern):
        visited_states = set()  # Keep track of visited states
        for i in range(n):
            current_state = tuple(self.data)  # Convert the map state to a hashable tuple
            if current_state in visited_states:
                print(f"Cycle detected at iteration #{i}, load: {self.calculateLoad()}")
                break  # Exit the loop if a cycle is detected
            visited_states.add(current_state)

            print("#" + str(i), self.calculateLoad())
            for p in pattern:
                self.shift(p)
    def calculateLoad(self):
        load = 0
        for y in range(self.h):
            for x in range(self.w):
                if self.get(x, y) == "O":
                    weight = self.h - y
                    load = load + weight
        return load


def getMap(source="real"):
    if source == "test":
        test_input = "../test.txt"
    else:
        test_input = "../input.txt"

    with open(test_input, "r") as f:
        lines = f.readlines()
        w = len(lines[0].strip())
        h = len(lines)
        m = Map(w, h)
        for y in range(h):
            for x in range(w):
                m.set(x, y, lines[y][x])
    return m

def main():
    x = getMap()
    #x.show()
    print("------")
    #x.shift()
    x.shiftNtimes(1000, ["N", "W", "S", "E"])
    #x.show()
    print("------")
    print(x.calculateLoad())

if __name__ == '__main__':
    main()