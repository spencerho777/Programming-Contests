import collections
import random


# test = open("a2tester.txt", 'w')
# test.write("800\n")
# letters = ["F", "O", "X"]
# for b in range(5):
#     test.write("1000\n")
#     for a in range(1000):
#         l = letters[random.randint(0, 2)]
#         test.write(l)
#     test.write("\n")



fin = open("a2tester.txt", 'r')
fout = open("a2bruteout.txt", 'w')


t = int(fin.readline().strip())


def solve(w):
    switch = 0
    firstO, firstX = w.find("O"), w.find("X")
    if firstO == -1 or (firstX < firstO and firstX != -1):
        onX = True
    else:
        onX = False
    for char in w:

        if char == "X":
            if not onX:
                switch += 1
                onX = True
        elif char == "O":
            if onX:
                switch += 1
                onX = False
    
    return switch

def bruteSolve():
    n = int(fin.readline().strip())
    w = fin.readline().strip()
    sol = 0
    for i in range(0, n):
        for j in range(i+1, n+1):
            #print(w[i:j], solve(w[i:j]))
            sol += solve(w[i:j])
    
    #print("\n")
    return sol

for case in range(t):
    fout.write("Case #{}: {}\n".format( case + 1, bruteSolve() ))

fout.close()
    
    
