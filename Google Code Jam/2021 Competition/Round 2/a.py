from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def computate(inp):

    
    
    return (dist[0] + dist[1])/k
for case in range(int(input())):
    inp = int(input())
    answer = computate(inp)
    print("Case #{}: {}".format( case + 1, answer ))
