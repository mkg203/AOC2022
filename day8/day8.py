def greaterchecker(arr, tree):
    visibleright = visibleleft = True
    for i in range(tree, len(arr)):
        if int(arr[tree]) <= int(arr[i]) and i != tree:
            visibleright = False
    for i in range(0, tree):
        if int(arr[tree]) <= int(arr[i]) and i != tree:
            visibleleft = False
    return visibleleft or visibleright

def scenicchecker(arr, tree):
    product1 = 0
    product2 = 0
    for i in range(tree + 1, len(arr)):
        product1 += 1
        if arr[tree] <= arr[i]:
            break
    for i in range(tree - 1, -1, -1):
        product2 += 1
        if arr[tree] <= arr[i]:
            break
        
    return product1 * product2

def column(string, i):
    n = ""
    for j in range(0, len(string)):
        n += string[j][i]
    return n

file = open("input")
arr = [x.strip() for x in file.readlines()]
visible = 0
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if i == 0 or j == 0 or i == len(arr) - 1 or j == len(arr[i]) - 1:
            visible += 1
        elif greaterchecker(arr[i], j) or greaterchecker(column(arr, j), i):
            visible += 1
print(visible)

points = []
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        points.append(scenicchecker(arr[i], j) * scenicchecker(column(arr, j), i))
print(max(points))
