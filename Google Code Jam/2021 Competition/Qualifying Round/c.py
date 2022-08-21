import itertools
def computate(n, c):
    l = [(a+1) for a in range(n)]
    cs = itertools.permutations(l, len(l))
    for d in cs:
        combo = list(d)
        #print(combo)
        if count(n, combo) == c:
            return " ".join([str(x) for x in combo])

    return "IMPOSSIBLE"

def count(n, inp):
    res = inp[:]
    c = 0
    for i in range(n-1):
        #print(res)
        mi = res.index(min(res[i:]))
        #print(res[i:mi+1][::-1])
        res[i:mi+1] = res[i:mi+1][::-1]
        #print((mi+1) - (i+1) + 1)
        c += (mi+1) - (i+1) + 1
        
    return c

for case in range(int(input())):
    inp = str(input()).split(" ")
    n, c = int(inp[0]), int(inp[1])
    answer = computate(n, c)
    print("Case #{}: {}".format( case + 1, answer ))

