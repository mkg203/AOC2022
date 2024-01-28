file = open("input")
arr = [x.strip() for x in file.readlines()]
signal = 0
x = 1
j = 1
for i in arr:
    if i == "noop":
        j += 1
    elif i.split(" ")[0] == "addx":
        j += 1
        if j == 220:
            signal += x * j
            # print(x, j)
            # print(signal)
            break
        if (j - 20) % 40 == 0:
            signal += x * j
            # print(x, j)
            # print(signal)
        j += 1 
        x += int(i.split(" ")[1])
    if (j - 20) % 40 == 0:
        signal += x * j
        # print(x, j)
        # print(signal)
print(signal)
