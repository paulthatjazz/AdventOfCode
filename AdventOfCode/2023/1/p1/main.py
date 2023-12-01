import re

file_path = "../input.txt"

res = 0


with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        digits = re.findall(r'\d', line,)
        
        code = str(digits[0]) + str(digits[-1])

        res += int(code)

print(res)
