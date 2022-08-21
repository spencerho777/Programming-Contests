
def computate(n, inp):
    pass
for case in range(int(input())):
    n = int(input())
    inp = [int(a) for a in str(input()).split(" ")]
    answer = computate(n, inp)
    print("Case #{}: {}".format( case + 1, answer ))
