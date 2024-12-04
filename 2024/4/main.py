import re

def load_wordsearch():
    lines = []
    with open("test.txt", "r") as file:
        data = file.readlines()
        # horizontal lines
        for line in data:
            lines.append(line.strip())
        # vertical lines
        for i in range(len(lines[0])):
            vertLine = "".join([line[i] for line in lines])
            lines.append(vertLine)
        # diagonal lines
    return lines

def count_word(lines, word):
    count = 0
    for line in lines:
        count += len(re.findall(word, line))
        count += len(re.findall(word[::-1], line))
    return count

def p1():
    lines = load_wordsearch()
    return count_word(lines, "XMAS")


if __name__ == "__main__":
    partOne = p1()
    print(f'Part 1: {partOne}')