import math
def getPascal(n):  
    pascal = [[] for _ in range(n)]
    for line in range(1, n+1):
        
        K = 1
        for i in range(1, line+1):
            pascal[line-1].append(K)
            K = int(K * (line-i) / i)
    return pascal
  

# MAXIMUM 30 levels of pascal
def solve(s):
    max_levels = int((math.log(s, 2) // 1) + 3)
    pascal = getPascal(max_levels)
    total = 1
    row = 0
    col = 0
    visited = [(0, 0)]
    while total != s:
        
        greed = 0
        if row == 0:
            row = 1
            col = 1
            total += 1
            visited.append((1,1))
        else:
            possible = []
            possible.append((total + pascal[row+1][col+1], 1, 1))
            possible.append((total + pascal[row+1][col], 1, 0))
            if col < row:
                #print(row, col)
                possible.append((total + pascal[row][col+1], 0, 1))
            if col > 0:
                possible.append((total + pascal[row][col-1], 0, -1))
            if row >= 2:
                possible.append((total + pascal[row-1][col-1], -1, -1))
                if col < row-1:
                    possible.append((total + pascal[row-1][col], -1, 0))
            possible = sorted(possible, key=lambda x: x[0], reverse=True)
            #print("POSSIBLE", possible)

            for a in possible:
                #print(a)
                loc = (row + a[1], col + a[2])
                if (a[0] <= s) and (loc not in visited):
                    total = a[0]
                    
                    print(total, loc, pascal[row+a[1]][col+a[2]])
                    visited.append(loc)
                    row += a[1]
                    col += a[2]
                    #print("CHOSE", loc, total)
                    break
            if total == s:
                break
            
    #print(visited)
    res = "\n"
    for loc in visited:
        res += str(loc[0] + 1) + " " + str(loc[1] + 1)
        res += "\n"
    res = res[:-1]
    return res


for case in range(int(input())):
    s = int(input())
    result = solve(s)
    print("Case #{}: {}".format( case + 1, result ))
