
### SUPER UNOPTIMIZED

def get_array(n):
    arr = []
    for x in range(n):
        line = [int(c) for c in str(input()).split(" ")]
        arr.append(line)
    print(arr)
    return arr
    
def get_trace(arr, n):
    s = 0
    for i in range(n):
        s += arr[i][i]
    return s

def find_dup_rows(arr, n):
    dups = 0
    for x in range(n):
        u = []
        for num in arr[x]:
            if num in u:
                dups += 1
                break
            else:
                u.append(num)
    return dups
            
def find_dup_cols(arr, n):
    dups = 0
    for x in range(n):
        u = []
        for y in range(n):
            #print(arr[y][x])
            if arr[y][x] in u:
                #print("dup")
                dups += 1
                break
            else:
                u.append(arr[y][x])
    return dups

for case in range(int(input())):
    n = int(input())
    arr = get_array(n)
    trace = get_trace(arr, n)
    rows = find_dup_rows(arr, n)
    cols = find_dup_cols(arr, n)
    
    answer = "0"
    print("Case #{}: {} {} {}".format( case + 1, trace, rows, cols ))
