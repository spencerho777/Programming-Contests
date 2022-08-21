def solve():
    inp = str(input()).split(" ")
    start = (int(inp[0]), int(inp[1]))
    ds = inp[2]
    
    for d in range(len(ds)):
        if ds[d] == "N":
            v = [0, 1]
        elif ds[d] == "S":
            v = [0, -1]
        elif ds[d] == "E":
            v = [1, 0]
        else:
            v = [-1, 0]
        start = (start[0] + v[0], start[1] + v[1])
        #print(start)
        if abs(start[0]) + abs(start[1]) <= d+1:
            return str(d+1)
    
    return "IMPOSSIBLE"


for case in range(int(input())):
    result = solve()
    print("Case #{}: {}".format( case + 1, result ))
