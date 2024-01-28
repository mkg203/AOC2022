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

def head(direction, hi): # moves head
    if direction == "U":
        hi[0] -= 1
    elif direction == "D": 
        hi[0] += 1
    elif direction == "L": 
        hi[1] -= 1
    elif direction == "R": 
        hi[1] += 1
    return hi

def mover(hi, ti):
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
    
file = open("input3")
arr = [x.strip() for x in file.readlines()]
ti = []
global tailindex
tailindex = []
for i in range(10):
    ti.append(list([0,0]))
for i in arr:
    direction, step = i.split(" ")
    step = int(step)
    while step != 0:
        ti[0] = head(direction, ti[0])
        for i in range(0, 9):
            if not proximity(ti[i], ti[i + 1]):
                ti[i + 1] = mover(ti[i], ti[i + 1])
        step -= 1
        tailindex.append((ti[-1][0], ti[-1][1]))
    
print(set(tailindex))
print(len(set(tailindex)))
