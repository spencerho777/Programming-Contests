
def interest(arr):
    s= 0

    print(arr)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][y] != -1:

                s += arr[x][y]
                #print(arr[x][y])
    return s

def eliminate(arr, l, w):
    c_arr = arr[:]
    neighbor_sum = 0
    ns = 0
    elims = 0
    total_i = 0
    while True:
        total_i += interest(arr)
        for row in range(l):
            arr = c_arr[:]
            for col in range(w):
                if row > 0:
                    if arr[row-1][col] != -1:
                        neighbor_sum += arr[row-1][col]
                        ns += 1
                if row < len(arr[row])-1:
                    if arr[row+1][col] != -1:
                        neighbor_sum += arr[row+1][col]
                        ns += 1
                if col > 0:
                    if arr[row][col-1] != -1:
                        neighbor_sum += arr[row][col-1]
                        ns += 1
                if col < len(arr[row])-1:
                    if arr[row][col-1] != -1:
                        neighbor_sum += arr[row][col-1]
                        ns += 1
            if ns != 0 and arr[row][col] < (neighbor_sum / ns):
                c_arr[row][col] = -1
                elims += 1
        if elims <= 0:
            break
    return total_i        

def solve(l, w):
    arr = [[-1 for _ in range(w)] for x in range(l)]
    for x in range(l):
        ls = str(input()).split(" ")
        #print(ls)
        if len(ls) > 1:
            for y in range(w):
                arr[x][y] = int(ls[y])
                    
    #print(arr)
    return str(eliminate(arr, l, w))
for case in range(int(input())):
    l, w = map(int, str(input()).split(" "))
    result = solve(l, w)
    print("Case #{}: {}".format( case + 1, result ))
