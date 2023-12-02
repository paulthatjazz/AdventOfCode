import re

file_path = "../input.txt"

RED_CUBES = 12
BLUE_CUBES = 14
GREEN_CUBES = 13
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

    game_no = re.findall(r"\d+", line)[0]
    games = line.split(";")
    
    for game in games:
        game = read_game(game)
        if game["greens"] > GREEN_CUBES or game["blues"] > BLUE_CUBES or game["reds"] > RED_CUBES:
            return 0

    return int(game_no)


with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        tot += read_line(line)

print(tot)