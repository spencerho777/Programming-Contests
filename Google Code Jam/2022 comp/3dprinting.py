
n = int(input())

def solve(printers):
    c, y, m, k = 0, 0, 0, 0
    c = min(printers[0][0], printers[1][0], printers[2][0])
    y = min(printers[0][1], printers[1][1], printers[2][1])
    m = min(printers[0][2], printers[1][2], printers[2][2])
    k = min(printers[0][3], printers[1][3], printers[2][3])
    s = c + y + m + k
    #print("S = ", s)
    if( s < 1000000):
        return "IMPOSSIBLE"
    
    colors = [c, y, m, k]
    dif = s - 1000000
    while dif > 0:
        #cnt+= 1
        #print(colors, dif)
        maxi = colors.index(max(colors))
        if colors[maxi] >= dif:
            colors[maxi] = colors[maxi] - dif
            break
        else:
            dif -= colors[maxi]
            colors[maxi] = 0

    colors = [str(x) for x in colors]
    return " ".join(colors)



for case in range(1, n+1):
    printers = []
    for _ in range(3):
        printers.append([int(x) for x in str(input()).split(" ")])

    print("Case #" + str(case) + ": " + solve(printers))