import re

def simulateRace(time, dist):
    possibleRecords = 0
    for i in range(time):
        holdDown = i
        speed = holdDown
        timeRemaining = time - holdDown
        distance = speed * timeRemaining
        if(distance >= dist):
            possibleRecords += 1
    return possibleRecords

def main():

    file_path = "../input.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()
        i = 0
        times = []
        dists = []
        for line in lines:
            nums = re.findall(r"\d+", line)
            if i == 0:
                times = nums
            else:
                dists = nums
            i += 1

        tot = 1

        for i in range(len(times)):
            times[i] = int(times[i])
            dists[i] = int(dists[i])
            poss = simulateRace(times[i], dists[i])
            print(poss)
            tot *= poss

        print(f"{tot} possible records, total")


if __name__ == "__main__":
    main()