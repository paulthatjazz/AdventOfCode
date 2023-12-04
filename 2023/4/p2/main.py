import re

def parseCard(card):

    score = 0

    nums = card.split("|")

    winning_nums = re.findall(r'\d+', nums[0])
    card_nums = re.findall(r'\d+', nums[1])
    game_no = winning_nums.pop(0)

    for num in winning_nums:
        if num in card_nums:
            score += 1

    extra_copies = []

    for i in range(score):
        extra_copies.append(int(game_no) + i + 1)

    return extra_copies

def main():

    file_path = "../input.txt"
    game_no = 0
    games = {}
    tot = 0

    with open(file_path, "r") as file:
        for line in file:
            game_no += 1

            if game_no in games:
                mult = games[game_no]+1
            else:
                mult = 1

            line = line.strip()
            extra_copies = parseCard(line)
            
            for copy in extra_copies:
                if copy in games:
                    games[copy] += mult
                else:
                    games[copy] = mult 
            tot += mult
    print(tot)


if __name__ == "__main__":
    main()