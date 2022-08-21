from collections import defaultdict
import math
import operator
from functools import reduce

def solve(s, diners):
    slices = []
    occ = defaultdict(lambda: 0)
    for x in input().split(" "):
        d = int(x)
        slices.append(d)
        occ[d] += 1
    
    S = sum(slices) / diners
    best = 0
    for key in occ:
        if key <= S and occ[key] > best:
            best = key
    if best == 0:
        sliceLength = S
    else:
        sliceLength = best
    print("SLICE LENGTH", sliceLength)
    cuts = 0
    num_slices = occ[sliceLength]
    slices = sorted(slices, key=lambda x: (x, x%s))
    #print(slices)
    i = 0

    while diners_left > 0:
        
    
    while num_slices < diners:
        new_slice = slices[i]
        if new_slice == sliceLength:
            i += 1
            continue
        #print(new_slice, math.fmod(new_slice, sliceLength))
        if math.fmod(new_slice, sliceLength) < 0.000000000000001:
            
            #print("-- slices, diners left", new_slice / sliceLength, diners - num_slices)
            if new_slice / sliceLength > diners - num_slices:
                #print("good, doesn't matter")
                cuts += diners - num_slices
                num_slices = diners
                
            else:
                #print("perfect")
                cuts += new_slice / sliceLength - 1
                num_slices += new_slice / sliceLength
        else:
            #print('eh')
            cuts += diners - num_slices
            num_slices = diners
            
        i += 1
    return str(int(cuts))


for case in range(int(input())):
    slices, diners = map(int, input().split(" "))
    result = solve(slices, diners)
    print("Case #{}: {}".format( case + 1, result ))
