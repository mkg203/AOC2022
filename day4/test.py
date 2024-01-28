def splitter(i):
    s1, s2 = i.split(',')
    a = [int(elem) for elem in (s1.split('-') + s2.split('-'))]
    print(a)
    return a
def checker(arr):
    return set(arr[0:2]).issuperset(set(arr[2:4])) or set(arr[2:4]).issuperset(set(arr[0:2]))
file = open("input2")
arr = file.readlines()
sum1 = 0
for i in arr:
    i = i[:-1]
    sum1 += checker(splitter(i))
print(sum1)
