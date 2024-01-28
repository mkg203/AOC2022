def check(string):
    # print(string)
    arr = [char for char in string]
    if len(string) > len(set(arr)):
        return False
    return True
file = open("input")
temp = file.readlines()
file.close()
string = temp[0]
# string = "bnppdvjthqldpwncqszvftbrmjlhg"
for i in range(0, len(string)):
    if check(string[i: i + 14]):
        print(i + 14)
        break
