
def make_consec(base, spaces):
    #print("base, spaces", base, spaces)
    new_int = str(base)
    while spaces > 0:
        base += 1
        spaces -= len(str(base))
        new_int += str(base)

    if spaces < 0:
        return -1 # not enough room
    else:
        return int(new_int)

def computate(n):
    length = len(str(n))
    if length == 1:
        return 12
    #print("length", length)
    answer = -1
    found = False
    for x in range(1, (length // 2) + 1):
        first = int(str(n)[:x])
        trigger = False
        while first < 10**x:
            #print(first)
            #first = int(str(n)[:x])
            first_l = len(str(first))
            spaces = length - x
            if not trigger and spaces % first_l != 0:
                trigger = True
                first = (10**x) - (spaces // first_l + 1)
            consec = make_consec(first, spaces)
            #print(consec)
            if consec == -1 or consec <= n:
                if found and consec > answer:
                    break
            else:
                found = True
                if answer == -1 or consec < answer:
                    answer = consec
                else:
                    break
            first += 1
    if answer == -1:
        #print("eh")
        answer = computate(10 ** (length))
    return answer

for case in range(int(input())):
    n = int(input())
    #inp = [int(a) for a in str(input()).split(" ")]
    
    answer = computate(n)
    print("Case #{}: {}".format( case + 1, answer ))
