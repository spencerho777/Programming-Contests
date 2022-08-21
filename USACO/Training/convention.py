"""
ID: spencewert
LANG: PYTHON3.4.0
PROG: convention
"""
import itertools
fin = open("convention.in", 'r')
fout = open("convention.out", 'w')

inp = str(fin.readline()).split(" ")
n, m, c = int(inp[0]), int(inp[1]), int(inp[2])
cows = sorted([int(x) for x in fin.readline().split(" ")])
# print(n, m, c)
# print(cows)

def checker(max_time):
    global cows, n, m, c
    buses = 1
    first_index = 0
    start_cow = cows[0]
    for a in range(1, len(cows)):
        if (cows[a] - start_cow > max_time) or (a + 1 - first_index > c):
            buses += 1
            start_cow = cows[a]
            first_index =  a
    return buses <= m

lo = 0
hi = (10 ** 9) - 1

def binary_search(lo, hi):
    if lo == hi:
        return lo
    if (lo+1) == hi:
        if checker(lo):
            return lo
        else:
            return hi
    mid = (lo + hi) // 2
    if checker(mid):
        return binary_search(lo, mid)
    else:
        return binary_search(mid+1, hi)



fout.write(str(binary_search(0, 10**9 - 1)))
fout.close()