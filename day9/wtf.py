def head(move, hi, ti): # moves head
    direction, step = move.split(" ")
    for i in range(0, int(step)):
        if direction == "U": hi[0] -= 1
            ti = tail(hi, ti)
        elif direction == "D": 
            hi[0] += 1
            ti = tail(hi, ti)
        elif direction == "L": 
            hi[1] -= 1
            ti = tail(hi, ti)
        elif direction == "R": 
            hi[1] += 1
            ti = tail(hi, ti)
    return hi, ti

def tail(hi, ti):
    global tailindex
    if proximity(hi, ti):
        return ti
    if hi[0] == ti[0]:
        if hi[1] > ti[1]:
            ti[1] += 1
        else:
            ti[1] -= 1
    elif hi[1] == ti[1]:
        if hi[0] > ti[0]:
            ti[0] += 1
        else:
            ti[0] -= 1
    else:
        if hi[0] > ti[0]:
            ti[0] += 1
        else:
            ti[0] -= 1
        if hi[1] > ti[1]:
            ti[1] += 1
        else:
            ti[1] -= 1
    return ti

def proximity(hi, ti):
    if ti == hi:
        return True
    elif ti[0] == hi[0]:
        if abs(ti[1] - hi[1]) == 1:
            return True
    elif ti[1] == hi[1]:
        if abs(ti[0] - hi[0]) == 1:
            return True
    if abs(ti[1] - hi[1]) == 1 and abs(ti[0] - hi[0]) == 1:
        return True
    return False

file = open("input3")
arr = [x.strip() for x in file.readlines()]
hi = [0, 0]
ti = []
for i in range(9):
    ti.append(list([0,0]))
print(ti)
global tailindex
tailindex = [[0, 0]]
for i in arr:
    print(ti)
    for j in range(0,9):
        print('lol',ti)
        if j == 0:
            hi, ti[0] = head(i, hi, ti[0])
        else:
            ti[j-1] = tail(ti[j-1], ti[j])
        if ti[-1] not in tailindex:
            tailindex.append(list(ti[-1]))
 
print(tailindex)
print(len(tailindex))
