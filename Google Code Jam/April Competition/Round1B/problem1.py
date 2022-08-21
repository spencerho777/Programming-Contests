import sys
import math

#UNSOLVED FOR NOW
def solve(x, y):
    if (x % 2 == 0 and y % 2 == 0 and x != 0 and y != 0) or (x % 2 != 0 and y % 2 != 0):
        return "IMPOSSIBLE"
    n_x = x < 0
    n_y = y < 0
    x1, y1 = bin(abs(x))[2:], bin(abs(y))[2:]
    y1 = list(y1.zfill(len(x1)))
    x1 = list(x1.zfill(len(y1)))
    print("BINARY", x1, y1)
    bsum = bin(abs(x)|abs(y))[2:][::-1] # REVERSED
    print("OR STATEMENT", bsum)
    x1 = x1[::-1]
    y1 = y1[::-1]
    availx, availy = [], []
    for bit in range(len(x1)):
        if x1[bit] == "1":
            availx.append(2 ** (bit + 1))
        if y1[bit] == "1":
            availy.append(2 ** (bit + 1))

    print(availx, availy)
    b = 0
    
    moves = []
    while b < len(bsum):
        bit = bsum[b]
        print(b, bit)
        if bit == "0" or (x1[b] == 1 and y1[b] == 1):
            if (2 ** b) not in availx and (2 ** b) not in availy:
                return "IMPOSSIBLE"
            else:
                if (2**b) in availx:
                    availx.remove(2**b)
                    x1[b] = "0"
                    m = "E"
                else:
                    availy.remove(2**b)
                    y1[b] = "0"
                    m = "S"
        else:
            if x1[b] == "0":
                m = "W"
            else:
                m = "N"
        """elif x1[b] == "1" and y1[b] == "1":
            if (2 ** b) not in availx and (2 ** b) not in availy:
                return "IMPOSSIBLE"
            else:
                print("double 1s changed")"""
        moves.append(m)
        b += 1
    return ''.join(moves)
     

for case in range(int(input())):
    x, y = map(int, str(input()).split(" "))
    result = solve(x, y)
    print("Case #{}: {}".format( case + 1, result ))
