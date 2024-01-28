from math import lcm

def op(i, num):
    l = lcm(23, 19, 13, 17)
    match i:
        case 0:
            num *= 19
            # num //= 3
            num %= l
            if num % 23 == 0:
                return num, 2
            return num, 3
        case 1:
            num += 6
            # num //= 3
            num %= l
            if num % 19 == 0:
                return num, 2
            return num, 0
        case 2:
            num *= num
            # num //= 3
            num %= l
            if num % 13 == 0:
                return num, 1
            return num, 3
        case 3:
            num += 3
            # num //= 3
            num %= l
            if num % 17 == 0:
                return num, 0
            return num, 1
