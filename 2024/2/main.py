import re

def loadReports():
    logs = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            vals = re.findall(r'\d+', line)
            logs.append(vals)
    return logs

def checkReport(nums):
    safe = True
    dir = None
    first = None
    for i in range(len(nums)):
        n = int(nums[i])
        if not safe:
            break
        else:
            if first is None:
                first = n
            else:
                prev = int(nums[i-1])

                if dir is None:
                    # if direction is not set get the direction, if no increase or decrease then it is not safe
                    if(n > prev):
                        dir = 1
                    elif(n < prev):
                        dir = -1
                    else:
                        safe = False
                else:
                    # if direction changes (from increasing to decreasing or vice versa) then it is not safe
                    if dir == 1:
                        if n < prev:
                            safe = False
                    else:
                        if n > prev:
                            safe = False

                # if difference between two numbers is greater than 3 or less than 1 then it is not safe
                diff = abs(n - prev)
                if diff > 3 or diff < 1:
                    safe = False
    return safe
    
def checkReports(problemDampener = False):
    logs = loadReports()
    safeCount = 0
    for log in logs:
        safe = False
        if problemDampener:
            for i in range(len(log)):
                c = log.copy()
                c.pop(i)
                safe = checkReport(c)
                if safe:
                    break
        else:
            safe = checkReport(log)
        if safe:
            safeCount += 1
    return safeCount

if __name__ == "__main__":
    p1Count = checkReports(False)
    p2Count = checkReports(True)
    print(f'Part 1: {p1Count}, Part 2: {p2Count}')