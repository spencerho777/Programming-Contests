

def nesting_depths(string):
    depths = [int(x) for x in list(string)]
    active_p = 0
    res = []
    for num in depths:
        if num > active_p:
            for _ in range(num - active_p):
                res.append("(")
            active_p = num
        elif num < active_p:
            for _ in range(active_p - num):
                res.append(")")
            active_p = num
        res.append(str(num))
    for _ in range(active_p):
        res.append(")")
    return ''.join(res)


for case in range(int(input())):
    string = str(input())
    answer = nesting_depths(string)
    
    print("Case #{}: {}".format( case + 1, answer ))
