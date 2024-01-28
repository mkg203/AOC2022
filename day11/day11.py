import op
            
file = open("input")
items = []
test = []
for i in file.readlines():
    if "Starting items:" in i:
        i = i.split(":")[1]
        items.append([int(x.strip()) for x in i.split(",")])
    elif "Test:" in i:
        test.append([int(x) for x in i.split() if x.isdigit()][0])
inspect = [0, 0, 0, 0, 0, 0, 0, 0]
for z in range(10_000):
    for i in range(0, len(items)):
        while len(items[i]) != 0:
            num, move = op.op(i, items[i].pop(0))
            items[move].append(num)
            inspect[i] += 1
    if z % 1000 == 0:
        print(inspect)
print(inspect)
m1, m2 = inspect.pop(inspect.index(max(inspect))), max(inspect)
print(m1, m2)
print(m1 * m2)
