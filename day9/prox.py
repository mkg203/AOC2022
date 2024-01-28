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
