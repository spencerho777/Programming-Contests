# """
# ID: spencewert
# LANG: PYTHON3.4.0
# PROG: daisy
# """
import collections
raw_inp = str(input()).split(" ")
n, q = int(raw_inp[0]), int(raw_inp[1])
prefix_solve = collections.deque()
suffix_solve = collections.deque()

for _ in range(q):
    raw_inp = str(input()).split(" ")
    a, b = int(raw_inp[0]), int(raw_inp[1])
    #fences.append([desired[:a-1], desired[b:]])
    print(prefix(a) + prefix(b))

