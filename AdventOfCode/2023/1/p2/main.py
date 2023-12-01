import regex as re

file_path = "../input.txt"

res = 0

num_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        digits = re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)


        for i in range(len(digits)):
            if digits[i].isnumeric() == False:
                digits[i] = num_map.get(digits[i])
        
        code = str(digits[0]) + str(digits[-1])

        res += int(code)

print(res)
