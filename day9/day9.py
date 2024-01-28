def head(move, hi, ti): # moves head
    direction, step = move.split(" ")
    for i in range(0, int(step)):
        if direction == "U":
            hi[0] -= 1
            ti = tail(hi, ti)
            # print(ti)
        elif direction == "D": 
            hi[0] += 1
            ti = tail(hi, ti)
        elif direction == "L": 
            hi[1] -= 1
            ti = tail(hi, ti)
        elif direction == "R": 
            hi[1] += 1
            ti = tail(hi, ti)
            # print("tail:", ti)
        # print(hi, ti)
    return hi, ti

def tail(hi, ti):
    global tailindex
    # print("in TAIL; head", hi, "tail", ti)
    # print("?? ?? ?? ??TAIL INDEX: ", tailindex)
        # print("TAIL INDEX: ", tailindex)
    # print(proximity(hi, ti))
    # print('checking proximity for ti:',ti,'and h1:',hi)
    if proximity(hi, ti):
        # print('in prox, ti:',ti)
        return ti
    # while proximity(hi, ti):
    if hi[0] == ti[0]:
        if hi[1] > ti[1]:
            ti[1] += 1
        else:
            ti[1] -= 1
        # add index of tail to a dictionary here
    elif hi[1] == ti[1]:
        if hi[0] > ti[0]:
            ti[0] += 1
        else:
            ti[0] -= 1
        # add index of tail to a dictionary here
    else:
        if hi[0] > ti[0]:
            ti[0] += 1
        else:
            ti[0] -= 1
        if hi[1] > ti[1]:
            ti[1] += 1
        else:
            ti[1] -= 1
    if ti not in tailindex:
        tailindex.append(list(ti))
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

# def pos(hi, ti) # defines how tail needs to move
file = open("input")
arr = [x.strip() for x in file.readlines()]
# print(proximity([3,2], [4,3]))
hi = [0, 0]
ti = [0, 0]
global tailindex
tailindex = []
tailindex.append([0, 0])
for i in arr:
    hi, ti = head(i, hi, ti)
print(tailindex)
print(len(tailindex))
