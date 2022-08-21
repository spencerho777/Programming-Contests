# """
# ID: spencewert
# LANG: PYTHON3.4.0
# PROG: daisy
# """
from string import ascii_uppercase
raw_inp = str(input()).split(" ")
n, q = int(raw_inp[0]), int(raw_inp[1])

alphabet = list(ascii_uppercase)
desired = str(input())
def min_paints(paint_list, s):
    s = list(s)
    sor = sorted(paint_list, reverse=True)
    #print(s, sor)
    a = 0
    paints = 0
    while a < len(sor):
        target = sor[a]
        active = False
        i = 0
        while i < len(s):
            #print(target, i)
            if s[i] == target:
                if not active:
                    #print("bam")
                    active = True
                    paints += 1
                del s[i]
                continue
            elif active:
                active = False
            i += 1
        a += 1
    return paints
        



for _ in range(q):
    raw_inp = str(input()).split(" ")
    a, b = int(raw_inp[0]), int(raw_inp[1])
    #fences.append([desired[:a-1], desired[b:]])
    print(min_paints(list(set(desired[:a-1])), desired[:a-1]) + min_paints(list(set(desired[b:])), desired[b:]))

