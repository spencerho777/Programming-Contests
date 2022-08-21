"""
ID: spencewert
LANG: PYTHON3.4.0
PROG: socdist2
"""

fin = open("socdist2.in", 'r')
num_cows = int(fin.readline())


fout = open("socdist2.out", 'w')

#num_cows = 6

sick = []
not_sick = []
cow_line = []
for i in range(num_cows):
    #temp = [2, 1]
    temp = str(fin.readline()).split()
    cow_pos, is_sick = int(temp[0]), int(temp[1])
    if is_sick:
        is_sick = True
        sick.append(cow_pos)
    else:
        not_sick.append(cow_pos)
    cow_line.append((cow_pos, is_sick))

"""
not_sick = [0, 10]
sick = [7, 1, 15, 3, 6]
cow_line = [(7, True),
            (1, True),
            (0, False),
            (15, True),
            (3, True),
            (10, False),
            (6, True)
]"""

cow_line = sorted(cow_line, key=lambda x:x[0])
print(cow_line)

r= float('inf')
for cow in not_sick:
    print([abs(x - cow) for x in sick])
    min_dist = min([abs(x - cow) for x in sick])

    r = min_dist if min_dist < r else r

print(r)


sick = sorted(sick)
prev = sick[0]
answer = 1
for c in range(1, len(sick)):
    if sick[c] - prev >= r:
        answer += 1
    prev = sick[c]

print(answer)
fout.write(str(answer))

fout.close()
