import collections
import random


test = open("a2tester.txt", 'w')
test.write("5\n")
letters = ["F", "O", "X"]
for b in range(5):
    test.write("800000\n")
    for a in range(800000):
        l = letters[random.randint(0, 2)]
        test.write(l)
    test.write("\n")



fin = open("a1sample.txt", 'r')
fout = open("a1out.txt", 'w')


t = int(fin.readline().strip())


def solve():
    n = int(fin.readline().strip())
    w = fin.readline().strip()
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
for case in range(t):
    fout.write("Case #{}: {}\n".format( case + 1, solve() ))

fout.close()
    
    
