
def computate(n, inp):
    
    #print(inp)
    last = inp[0]
    added_digits = 0
    d = 0
    a = 0
    dig = [last]
    for i in inp[1:]:
        if i > last+a:
            last = i
            a = 0
            dig.append(last + a)
            continue
        #print("last, i:", last+a, i)
        idig = len(str(i))
        ldigc = len(str(last))
        d = ldigc - idig
        if d == 0:
            if last + a >= i:
                d += 1
                a = 0
        elif last - i * (10**d) >= ((10**d)-1):
            
            d += 1
            a = 0
        
        elif last == i * (10**d):
            #print("a,d",a, 9 * (10**(d-1)))
            if d == 0 or a >= ((10**d)-1):
                #print('reset')
                d += 1
                a = 0
            else:
                a += 1
        elif last-i*(10**d) > 0 and last - i * (10**d) < ((10**d)-1):
            
            a = last - i * (10**d) + 1
        elif last<i*(10**d):
            a = 0
        added_digits += d
        #print("\t",d)
        last = i * (10 ** d)
        dig.append(last + a)
    # print(inp)
    #print(dig)
    return added_digits

print("ANSWER", computate(1, [1, 1, 1, 1, 1, 2]))
for case in range(int(input())):
    n = int(input())
    inp = [int(a) for a in str(input()).split(" ")]
    answer = computate(n, inp)
    print("Case #{}: {}".format( case + 1, answer ))
