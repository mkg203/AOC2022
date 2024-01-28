def sumdir(arr):
    increment = 0
    for i in range(0, len(arr)):
        if arr[i][0].isdigit():
            increment += int(arr[i].split(" ")[0])
    return increment #if increment < 100000 else 0
def dirsize(arr):
    increment = 0
    cdcount = 1
    for i in range(0, len(arr)):
        if arr[i][0].isdigit():
            increment += int(arr[i].split(" ")[0])
        elif arr[i].split(" ")[1] == "cd" and arr[i].split(" ")[2] != "..":
            cdcount += 1
        elif arr[i] == "$ cd ..":
            cdcount -= 1
        if cdcount == 0:
            break
    return increment
    
file = open("input")
arr = [x.strip() for x in file.readlines()]
sum1 = 0
sum1 += sumdir(arr)
print(sum1)
darr = []
for i in range(0, len(arr)):
    if arr[i] == "$ ls":
        darr.append(dirsize(arr[i + 1:]))
darr = sorted(darr)
for i in range(0, len(darr)):
    if dirarr[i] >= 3837783:
        print(dirarr[i])
        break
