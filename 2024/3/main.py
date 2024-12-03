import re

def load_data():
    with open("input.txt", "r") as file:
        data = file.readlines()
        return ''.join(data)

def p1():
    data = load_data()
    mul_fns = re.findall(r"mul\(\d+\,\d+\)", data)
    sum = 0
    for fn in mul_fns:
        nums = re.findall(r"\d+", fn)
        res = int(nums[0]) * int(nums[1])
        sum += res
    return sum

def p2():
    data = load_data()
    mul_fns = re.findall(r"mul\(\d+\,\d+\)|do\(\)|don't\(\)", data)
    sum = 0
    do = True
    for fn in mul_fns:
        nums = re.findall(r"\d+", fn)
        if(len(nums) == 0):
            if "don" in fn:
                do = False
            else:
                do = True
        else:
            if do:
                sum += (int(nums[0]) * int(nums[1]))
    return sum

if __name__ == "__main__":
    partOne = p1()
    partTwo = p2()
    print(f'Part 1: {partOne}, Part 2: {partTwo}')
