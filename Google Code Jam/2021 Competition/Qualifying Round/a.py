
def computate(n, inp):
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


answer = computate(7, [int(a) for a in str(input()).split(" ")])
print(answer)
for case in range(int(input())):
    n = int(input())
    inp = [int(a) for a in str(input()).split(" ")]
    answer = computate(n, inp)
    print("Case #{}: {}".format( case + 1, answer ))
