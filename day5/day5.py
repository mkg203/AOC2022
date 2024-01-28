def mover(steps, matrix):
    piece = matrix[len(matrix) - steps:]
    piece = piece[::-1]
    matrix = matrix[:-steps]
    return piece, matrix
def splitter(i):
    s1, s2 = i.split(" from ")
    s1, n1 = s1.split(" ")
    n2, n3 = s2.split(" to ")
    return int(n1), int(n2) - 1, int(n3) - 1
matrix = ["DHNQTWVB", "DWB", "TSQWJC", "FJRNZTP", "GOVJMST", "BWFTN", "BLDQFHVN", "HPFR", "ZSMBLNPH"]
file = open("input")
for i in file.readlines():
    i = i[:-1]
    guide = splitter(i) # index 0 of guide is number of pieces to be moved
    piece, matrix[guide[1]] = (mover(guide[0], matrix[guide[1]])) # index 1 is the index of the source
    matrix[guide[2]] += piece # index 2 is the index of the destination
print(*matrix)
file.close()
