import collections
import random

fin = open("breal.txt", 'r')
fout = open("bout.txt", 'w')


t = int(fin.readline().strip())

finalGraph = []
def solve():
    global finalGraph
    inp = str(fin.readline().strip()).split(" ")
    n, m, a, b = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])

    dist = n + m - 2
    corner1 = a - dist
    corner2 = b - dist
    graph = []
    if corner1 <= 0 or corner2 <= 0:
        return "Impossible"

    else:
        graph.append([])
        graph[0].append(corner1)
        for _ in range(m-2):
            graph[0].append(1)
        graph[0].append(corner2)

        for _ in range(n-1):
            graph.append([1 for _ in range(m)])

        finalGraph = graph
        return "Possible"

    
for case in range(t):
    sol = solve()
    fout.write("Case #{}: {}\n".format( case + 1, sol))
    if sol == "Possible":
        for row in finalGraph:
            stringRow = [str(i) for i in row]
            fout.write(" ".join(stringRow) + "\n")


fout.close()
    
    
