
t = int(input())

def solve(n, dice):

    sor = sorted(dice)
    need = 1
    for x in range(len(sor)):
        #print(sor[x], need)
        if sor[x] >= need:
            need += 1
        else:
            continue
    return str(need-1)

for case in range(1, t+1):
    n = int(input())
    dice = [int(x) for x in str(input()).split(" ")]

    print("Case #" + str(case) + ": " + solve(n, dice))