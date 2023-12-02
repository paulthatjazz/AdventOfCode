import re
from math import prod

file_path = "../input.txt"

tot = 0

def read_game(line):
    greens = re.findall(r"\d+\sgreen", line)
    greens = [int(green.split()[0]) for green in greens]

    blues = re.findall(r"\d+\sblue", line)
    blues = [int(blue.split()[0]) for blue in blues]

    reds = re.findall(r"\d+\sred", line)
    reds = [int(red.split()[0]) for red in reds]

    return { "greens": sum(greens), "blues": sum(blues), "reds": sum(reds) }


def read_line(line):

    min_green = 0
    min_blue = 0
    min_red = 0

    game_no = re.findall(r"\d+", line)[0]
    games = line.split(";")
    
    for game in games:
        game = read_game(game)

        min_green = max(min_green, game["greens"])
        min_blue = max(min_blue, game["blues"])
        min_red = max(min_red, game["reds"])


    return prod([min_green, min_blue, min_red])


with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        tot += read_line(line)

print(tot)