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


        times = int(''.join(str(t) for t in times))
        dists = int(''.join(str(d) for d in dists))

        poss = simulateRace(times, dists)

        print(f"{poss} possible records")


if __name__ == "__main__":
    main()