import re
from collections import Counter

def readAsLists():

    l1, l2 = [], []

    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            vals = re.findall(r'\d+', line)
            l1.append(int(vals[0]))
            l2.append(int(vals[1]))
        return l1, l2

def partOne():
    l1, l2 = readAsLists()

    l1.sort()
    l2.sort()

    sumOfDiff = 0
    for i in range(len(l1)):
        sumOfDiff += abs(l1[i] - l2[i])

    return sumOfDiff

def partTwo():
    l1, l2 = readAsLists()

    count = Counter(l2)

    sumSimilar = 0
    for i in range(len(l1)):
        if l1[i] in count:
            sumSimilar += (l1[i] * count[l1[i]])

    return sumSimilar

if __name__ == "__main__":
    p1 = partOne()
    p2 = partTwo()
    print(f'Part 1: {p1}, Part 2: {p2}')