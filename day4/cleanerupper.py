def container(ele):
    a = [int(ele[:ele.index('-')]), int(ele[ele.index(',') + 1: ele.rindex('-')]), int(ele[ele.index('-') + 1: ele.index(',')]), int(ele[ele.rindex('-') + 1: len(ele)])]
    print(a)
    if a[0] <= a[1] and  a[2] >= a[3] or a[1] <= a[0] and a[3] >= a[2]:
        return 1
    return 0
file = open("input2")
arr = file.readlines()
sum1 = 0
for i in arr:
    i=i[:-1]
    sum1 += container(i)
print(sum1)

