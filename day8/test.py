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
        
    print(product1, product2)
    return product1 * product2

points = []
points.append(scenicchecker("33549", 2) * scenicchecker("35353", 3))
print(max(points))
