
from collections import Counter
from functools import cmp_to_key
import re

card_values = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2 }

def parseHand(hand):
    counts = sorted(Counter(hand).values(), reverse=True)
    if counts == [5]:
        return 10
    elif counts == [4, 1]:
        return 9
    elif counts == [3, 2]:
        return 8
    elif counts == [3, 1, 1]:
        return 7
    elif counts == [2, 2, 1]:
        return 6
    elif counts == [2, 1, 1, 1]:
        return 5
    elif counts == [1, 1, 1, 1, 1]:
        return 4

def parseLine(line):
    hand = re.findall(r"\w+", line)[0].strip()
    bet = int(re.findall(r"\w+", line)[1])
    rank = parseHand(hand)
    return rank, bet, hand

def compareHands(hand1, hand2):
    if hand1[0] > hand2[0]:
        return 1
    elif hand1[0] < hand2[0]:
        return -1
    else:
        for i in range(0, 5):
            if card_values[hand1[2][i]] > card_values[hand2[2][i]]:
                return 1
            elif card_values[hand1[2][i]] < card_values[hand2[2][i]]:
                return -1
        
def sortHands(arr):
    return sorted(arr, key=cmp_to_key(compareHands))

def applyWinnings(arr):
    rank = 1
    total_winnings = 0
    for hand in arr:
        total_winnings += hand[1] * rank
        rank += 1
    return total_winnings

def main():
    file_path = "../input.txt"
    arr = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            arr.append(parseLine(line))

    arr = sortHands(arr)

    print(applyWinnings(arr))

if __name__ == "__main__":
    main()