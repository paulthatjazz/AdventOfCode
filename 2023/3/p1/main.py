
file_path = "../input.txt"

arr = []

def getCode(arr, width, x, y):
    code = arr[y * width + x]

    valid = True
    tx = x - 1
    while valid:
        if tx != -1:
            # check left
            if arr[y * width + tx].isnumeric():
                code = arr[y * width + tx] +  code 
            else:
                valid = False
        else:
            valid = False
        tx -= 1

    valid = True
    tx = x + 1
    while valid:
        if tx != width:
            # check right
            if arr[y * width + tx].isnumeric():
                code += arr[y * width + tx]
            else:
                valid = False
        else:
            valid = False
        tx += 1

    return int(code)



    

def getCodes(arr, width, x, y):

    codes = []
    
    if y != 0:
        # check up
        if arr[(y - 1) * width + x].isnumeric():
            codes.append(getCode(arr, width, x, y - 1))

    if y != len(arr) // width - 1:
        # check down
        if arr[(y + 1) * width + x].isnumeric():
            codes.append(getCode(arr, width, x, y + 1))

    if x != width - 1:
        # check right
        if arr[y * width + x + 1].isnumeric():
            codes.append(getCode(arr, width, x + 1, y))
        
        if y != 0:
        # check up right
            if arr[(y - 1) * width + x + 1].isnumeric():
                codes.append(getCode(arr, width, x + 1, y - 1))
            
        
        if y != len(arr) // width - 1:
            # check down right
            if arr[(y + 1) * width + x + 1].isnumeric():
                codes.append(getCode(arr, width, x + 1, y + 1))
            
        
    if x != 0:
        # check left
        if arr[y * width + x - 1].isnumeric():
            codes.append(getCode(arr, width, x - 1, y))
        
        if y != 0:
        # check up left
            if arr[(y - 1) * width + x - 1].isnumeric():
                codes.append(getCode(arr, width, x - 1, y - 1))
            
        if y != len(arr) // width - 1:
            # check down left
            if arr[(y + 1) * width + x - 1].isnumeric():
                codes.append(getCode(arr, width, x - 1, y + 1))

    return list(set(codes))



with open(file_path, "r") as file:
    w = 0
    codes = []
    for line in file:
        w = max(w, len(line))
        for ch in line:
            arr.append(ch)

    
    for idx, i in enumerate(arr):
        if i != "." and i != "\n":
            x = idx % w
            y = idx // w
            if not i.isnumeric():
                # scan for code
                code = getCodes(arr, w, x, y)

                for c in code:
                    codes.append(c)
    
    print(sum(codes))
