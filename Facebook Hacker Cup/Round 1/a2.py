import collections
import random


# test = open("a1tester.txt", 'w')
# test.write("80\n")
# letters = ["F", "O", "X"]
# for b in range(80):
#     test.write("50000\n")
#     for a in range(50000):
#         l = letters[random.randint(0, 2)]
#         test.write(l)
#     test.write("\n")



fin = open("a2tester.txt", 'r')
fout = open("a2out.txt", 'w')


t = int(fin.readline().strip())


def solve():
    changeList = []
    n = int(fin.readline().strip())
    w = fin.readline().strip()
    switch = 0
    firstO, firstX = w.find("O"), w.find("X")
    if firstO == -1 or (firstX < firstO and firstX != -1):
        onX = True
        if firstX == -1:
            return 0
        changeList.append(firstX)
    else:
        onX = False
        if firstO == -1:
            return 0
        changeList.append(firstO)


    for c in range(len(w)):

        if w[c] == "X":
            if not onX:
                switch += 1
                onX = True
                changeList.append(c) 
        elif w[c] == "O":
            if onX:
                switch += 1
                onX = False
                changeList.append(c)
    
    return switch
for case in range(t):
    fout.write("Case #{}: {}\n".format( case + 1, solve() ))

fout.close()
