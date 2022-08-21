"""
ID: spencewert
LANG: PYTHON3.4.0
PROG: tracing
"""

class Cow:
    def __init__(self, n):
        self.n = n
        self.interactions = {}
        self.first = float('inf')

    def add_interaction(self, t, dif_cow):
        self.interactions[t] = dif_cow
    def def_first(self, t):
        if self.first > t:
            self.first = t
    def interactions_past_t(self, t, k):
        interactions_past = []
        for l in self.interactions:
            if l >= t:
                interactions_past.append(self.interactions[l])
            if len(interactions_past) >= k:
                break
        if len(interactions_past) > k:
            return interactions_past[:k]
        return interactions_past
    def __str__(self):
        return str(self.n) + " " + str(self.is_sick)

def all_touched(start_cow, t, k, all_cows, sick): #BFS kind of

    data = []
    infected = [start_cow]
    queue = []

    for c in start_cow.interactions_past_t(t, k):
        if c not in infected:
            queue.append(c)
    
    while queue:
        cow = queue.pop(0)
        infected.append(cow)
        """if len(infected) > sick:
            return 0"""
        for c in cow.interactions_past_t(t, k):
            if c not in infected:
                queue.append(c)
        
    return len(infected)
    
        

####### need to find patient zero
####### K is the number of hooves shaked before they stop becoming infectious

fin = open("tracing.in", 'r')

fout = open("tracing.out", 'w')

temp = str(fin.readline().strip()).split()
sick = str(fin.readline().strip()).count('1')


def define_cow(cow, t, another_cow):
    cow.def_first(t)
    cow.add_interaction(t, another_cow)

#print(sick, temp)

#print(temp)
#sick = 2
#temp = [4, 3]
num_cows, times = int(temp[0]), int(temp[1])



all_cows = [Cow(i) for i in range(num_cows)]

inp = [(7, 1, 2),
    (5, 2, 3),
    (6,2,4)]



for interaction in range(times):
    temp = str(fin.readline()).split()
    #temp = inp[interaction]
    t, c1, c2 = int(temp[0]), int(temp[1]), int(temp[2])
    cow1 = all_cows[c1-1]
    cow2 = all_cows[c2-1]
    define_cow(cow1, t, cow2)
    define_cow(cow2, 2, cow1)


k = 0
exi = False
while True:
    for cow in all_cows:
        s = all_touched(cow, cow.first, k, all_cows, sick)
        if s == sick:
            p_zero = cow
            exi = True
            break
    if not exi:
        k += 1
    else:
        break

if all_touched(p_zero, p_zero.first, 100, all_cows, sick) == sick:
    bound = "Infinity"
else:
    bound = k

print(str(p_zero.n + 1) + " " + str(k) + " " + str(bound))
fout.write(str(p_zero.n + 1) + " " + str(k) + " " + str(bound))

fout.close()
