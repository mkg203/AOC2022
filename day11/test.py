import op2 as e
            
file = open("input2")
items = []
test = []
for i in file.readlines():
    if "Starting items:" in i:
        i = i.split(":")[1]
        items.append([int(x.strip()) for x in i.split(",")])
    elif "Test:" in i:
        test.append([int(x) for x in i.split() if x.isdigit()][0])
inspect = [0, 0, 0, 0]


for z in range(10_000):
    for i in range(0, len(items)):
        while len(items[i]) != 0:
            num, move = e.op(i, items[i].pop(0))
            items[move].append(num)
            inspect[i] +=1
print(inspect)
print(items)
