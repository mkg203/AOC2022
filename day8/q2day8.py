def column(string, i):
    n = ""
    for j in range(0, len(string)):
        n += string[j][i]
    return n

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

points = []
file = open("input")
arr = [x.strip() for x in file.readlines()]
points = []
for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        points.append(scenicchecker(arr[i], j) * scenicchecker(column(arr, j), i))
print(max(points))
