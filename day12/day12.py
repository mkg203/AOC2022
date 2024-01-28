S = (21, 0)
file = open("input")
arr = [x.strip() for x in file.readlines()]
for i in range(0, len(arr)):
    try:
        if arr[i].index("E") >= 0:
            E = (i, arr[i].index("E"))
    except ValueError:
        continue
print(S, E)
