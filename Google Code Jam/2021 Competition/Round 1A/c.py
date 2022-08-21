
def binary_counter(n, bits, i):
    global inp, s_inp
    #print(n, bits, i)
    if i == n:
        s = 0
        p = 1
        for k in range(n):
            if bits[k] == 0:
                s += inp[k]
            else:
                p *= inp[k]
                if p >= s_inp:
                    return
        if s == p:
            works.append(s)

        return

    bits[i] = 0
    binary_counter(n, bits, i + 1)

    bits[i] = 1
    binary_counter(n, bits, i + 1)

def computate(inp):
    global works
    binary_counter(len(inp), [None] * len(inp), 0)
    return max(works)
for case in range(int(input())):
    global inp, s_inp, works
    n = int(input())
    inp = []
    works = [0]
    s_inp = 0
    for i in range(n):
        r_inp = str(input()).split(" ")
        inp += [int(r_inp[0])] * int(r_inp[1])
        s_inp = sum(inp)
    answer = computate(inp)
    print("Case #{}: {}".format( case + 1, answer ))
