
class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = [0] * w * h
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
    def shift(self):
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
    x.show()
    print("------")
    x.shift()
    x.show()
    print("------")
    print(x.calculateLoad())

if __name__ == '__main__':
    main()