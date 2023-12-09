def calcSteps(history):
    steps = [0] * (len(history)-1)
    for i in range(len(history)-1):
        steps[i] = int(history[i+1]) - int(history[i])
    return steps


def parseInput(source):
    if source == "test":
        test_input = "../test.txt"
    else:
        test_input = "../input.txt"

    arr = []

    with open(test_input, "r") as f:
        lines = f.readlines()
        for line in lines:
            arr2 = []
            history = line.split(" ")
            y = calcSteps(history)
            arr2.append(history)
            arr2.append(y)
            while y.count(0) != len(y):
                y = calcSteps(y)
                arr2.append(y)
            arr.append(arr2)
            print("-------------------")
            for a in arr2:
                print(a)
    return arr

def extrapolateNextSteps(arr):
    tot = 0
    for a in arr:
        step = 0
        prediction = 0    
        for i, b in enumerate(reversed(a)):
            if len(b) == 1:
                step +=0
            else:
                step += int(b[-1]) - int(b[-2])
            prediction = int(b[-1]) + int(step)
            b.append(prediction)
        tot += prediction
    return tot


def main():
    x = parseInput("real")
    y = extrapolateNextSteps(x)
    print(y)

if __name__ == "__main__":
    main()