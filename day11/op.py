from math import lcm

def op(i, num):
    l = lcm(11, 2, 5, 17, 19, 7, 3, 13)
    match i:
        case 0:
            num *= 5
            # num //= 3
            num %= l
            if num % 11 == 0:
                return num, 3
            return num, 4
        case 1:
            num *= num
            # num //= 3
            num %= l
            if num % 2 == 0:
                return num, 6
            return num, 7
        case 2:
            num *= 7
            # num //= 3
            num %= l
            if num % 5 == 0:
                return num, 1
            return num, 5
        case 3:
            num += 1
            # num //= 3
            num %= l
            if num % 17 == 0:
                return num, 2
            return num, 5
        case 4:
            num += 3
            # num //= 3
            num %= l
            if num % 19 == 0:
                return num, 2
            return num, 3
        case 5:
            num += 5
            # num //= 3
            num %= l
            if num % 7 == 0:
                return num, 1
            return num, 6
        case 6:
            num += 8
            # num //= 3
            num %= l
            if num % 3 == 0:
                return num, 0
            return num, 7
        case 7:
            num += 2
            # num //= 3
            num %= l
            if num % 13 == 0:
                return num, 4
            return num, 0
