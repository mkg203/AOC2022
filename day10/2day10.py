def display(x):
    for i in range(0, 40):
        if i + 1 == x or i == x or i - 1 == x: 
            return "#"
    return "."
def row(j):
    if j <= 40:
        return 0
    elif j <= 80:
        return 1
    elif j <= 120:
        return 2
    elif j <= 160:
        return 3
    elif j <= 200:
        return 4
    else:
        return 5
    
file = open("input")
arr = [x.strip() for x in file.readlines()]
signal = 0
disp = [[], [], [], [], [], []]
x = 1
j = 1
for i in arr:
    if i == "noop":
        j += 1
        disp[row(j)] += display(x)
    elif i.split(" ")[0] == "addx":
        j += 1
        disp[row(j)] += display(x)
        # if j == 220:
        #     signal += x * j
        #     break
        # if (j - 20) % 40 == 0:
        #     signal += x * j
        j += 1 
        disp[row(j)] += display(x)
        x += int(i.split(" ")[1])
    # if (j - 20) % 40 == 0:
    #     signal += x * j
# print(signal)
print("check")
print(disp)
