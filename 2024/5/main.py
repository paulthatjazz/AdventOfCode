def loadInputs():
    with open ('test.txt', 'r') as f:
        rules = []
        printingOrder = []
        for line in f:
            if "|" in line:
                rule = line.strip().split("|")
                rules.append(rule)
            elif "," in line:
                printingOrder.append(line.strip().split(","))
            else:
                continue

    return rules, printingOrder

def checkOrderP1(rules, order):
    return 0

        

def partOne():
    rules, printingOrder = loadInputs()
    res = 0
    for i in printingOrder:
        res += checkOrderP1(rules, i)
    return res

if __name__ == "__main__":
    p1 = partOne()
    print(f'Part 1: {p1}')