import re
import random

def loadInputs():
    with open ('test.txt', 'r') as f:
        rules = []
        printingOrder = []
        for line in f:
            if "|" in line:
                rule = line.strip().split("|")
                rules.append(rule)
            elif "," in line:
                nums = re.findall(r'\d+', line)
                printingOrder.append(nums)
            else:
                continue

    return rules, printingOrder


def checkPageWithRule(page, rule):
    x, y = rule[0], rule[1]
    if x in page and y in page:
        idx_x = page.index(x)
        idx_y = page.index(y)
        return (idx_x < idx_y)
    else:
        return True

def checkOrder(rules, order):
    midPage = order[int((len(order) - 1)/2)]
    for rule in rules:
        ruleCheck = checkPageWithRule(order, rule)
        if not ruleCheck:
            midPage = 0
            break
    return int(midPage)

def reOrder(rules, order):
    # TODO: Doesn't work, need to re-think this approach
    correctOrder = False
    newOrder = order.copy()
    print(f'Order: {order}')
    while not correctOrder:
        for rule in rules:
            if not checkPageWithRule(order, rule):
                x, y = rule[0], rule[1]
                joyDivision = []
                for page in newOrder:
                    if page == x:
                        joyDivision.append(x)
                        joyDivision.append(y)
                    elif page != y:
                        joyDivision.append(page)
                print(f'Joy Division: {joyDivision}')
                newOrder = joyDivision
                correctOrder = checkOrder(rules, newOrder)
    midPage = newOrder[int((len(order) - 1)/2)]
    return int(midPage)

def main(reorder = False):
    rules, printingOrder = loadInputs()
    res = 0
    for i in printingOrder:
        if reorder:
            m = checkOrder(rules, i)
            if m == 0:
                res += reOrder(rules, i)
        else:
            res += checkOrder(rules, i)
    return res

if __name__ == "__main__":
    p1 = main()
    p2 = main(True)
    print(f'Part 1: {p1},  Part 2: {p2}')