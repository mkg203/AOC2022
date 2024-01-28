def finder(i):
    s = ""
    for j in range(0, len(i) // 2):
        for k in range(len(i) // 2, len(i)):
            if i[j] == i[k]:
                s += i[j]
                return s
def value(s):
    sum1 = 0
    for i in s:
        if i.isupper():
            sum1 += ord(i) - 38
        else:
            sum1 += ord(i) - 96
    return sum1
def badges(arr):
    s = ""
    for i in range(0, len(arr), 3):
        for j in arr[i]:
            for k in arr[i + 1]:
                for l in arr[i + 2]:
                    if j == k and k == l:
                        s += j
                        break;
                if j == k and k == l:
                    break;
            if j == k and k == l:
                break;
    return s
        
file = open("input")
arr = file.readlines()
s = ""
for i in arr:
    s += finder(i)
print(s)
print(value(s))
s = badges(arr)
print(s)
print(value(s))
