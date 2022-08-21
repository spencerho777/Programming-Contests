
def parenting(acts):
    s = []
    for i in range(acts):
        start, stop = map(int, str(input()).split(" "))
        s.append( (start, stop, i) )
    s = sorted(s, key=lambda x: x[0])
    #print(s)
    J, C = (0, 0), (0, 0)
    res= []
    for act in s:
        if act[0] >= J[1]:
            res.append( ("J", act[2]) )
            J = act
        elif act[0] >= C[1]:
            res.append( ("C", act[2]) )
            C = act
        else:
            res = ['I', 'M', 'P', 'O', 'S', 'S', 'I', 'B', 'L', 'E']
            break
    if type(res[0]) != str:
        res = [c[0] for c in sorted(res, key=lambda x: x[1])]
    return ''.join(res)
for case in range(int(input())):
    acts = int(input())
    answer = parenting(acts)
    
    print("Case #{}: {}".format( case + 1, answer ))

