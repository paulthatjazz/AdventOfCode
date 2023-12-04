import re

def parseCard(card):

    score = 0

    nums = card.split("|")

    winning_nums = re.findall(r'\d+', nums[0])
    card_nums = re.findall(r'\d+', nums[1])
    game_no = winning_nums.pop(0)

    for num in winning_nums:
        if num in card_nums:
            if score == 0:
                score = 1
            else: 
                score *= 2

    return score


def main():

    file_path = "../input.txt"

    tot = 0

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            tot += parseCard(line)
    print(tot)


if __name__ == "__main__":
    main()