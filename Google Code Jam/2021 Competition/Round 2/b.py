
r_inp = str(input()).split(" ")
t = int(r_inp[0])
for case in range(t):
    n = int(r_inp[1])
    #coins = 0
    sor = 1
    while sor < n:
        print("M " + str(sor) + " " + str(n))
        inp = int(input())
        if inp== -1:
            raise Exception("kys")
        if inp != sor:
            print("S " + str(sor) + " " + str(inp))
        sor += 1
        yes = int(input())
        if yes == -1:
            raise Exception("kys")
        #coins += (10**8 // (n-sor+1))
    print("D")
    #print(coins - ((10 ** 8)*6))
    yes = int(input())
    if yes == -1:
        raise Exception("kys")
    
    
