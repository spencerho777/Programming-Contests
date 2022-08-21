import collections
import math
visited = collections.defaultdict(bool)

def invertBits(num): 
    if num == 0:
        return 1
    x = int(math.log2(num)) + 1
    for i in range(x): 
        num = (num ^ (1 << i)) 
      
    return num
  
def computate(start, target, moves=0):
    #print(start)
    if start == target:
        return moves
    if moves >= 10:
        return 20
    
    answer = computate(start*2, target, moves+1)
    answer2 = computate(invertBits(start), target, moves+1)
    a = min(answer, answer2)
    return a
for case in range(int(input())):
    n = str(input()).split(" ")
    start, target = int(n[0]), int(n[1])
    answer = computate(start, target)
    if answer == 20:
        answer = "IMPOSSIBLE"
    print("Case #{}: {}".format( case + 1, answer ))
