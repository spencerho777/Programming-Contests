"""
ID: spencewert
LANG: PYTHON3.4.0
PROG: perimeter
"""
from collections import deque
fin = open("perimeter.in", 'r')
fout = open("perimeter.out", 'w')

n = int(fin.readline())
graph = []
for _ in range(n):
    graph.append(list(fin.readline().strip()))
visited = [[False for _ in range(n)] for _ in range(n)]
# print(visited)

# def print_graph(graph, n):
#     for m in range(n):
#         print(graph[m])
#     print("\n\n")

# print_graph(graph, n)

def flood(x, y):
    global n, visited, graph
    queue = deque()
    queue.append((x, y))
    a, p = 0, 0
    # print("started: ", x, y)
    while queue:
        i, j = queue.pop()
        # print(i, j)
        if not visited[i][j]:
            visited[i][j] = True
            #print_graph(visited, n)
            a += 1
            if i > 0 and graph[i-1][j] == "#":
                if not visited[i-1][j]:
                    queue.append((i-1, j))
            else:
                p += 1

            if i < n-1 and graph[i+1][j] == "#":
                if not visited[i+1][j]:
                    queue.append((i+1, j))
            else:
                p += 1

            if j > 0 and graph[i][j-1] == "#":
                if not visited[i][j-1]:
                    queue.append((i, j-1))
            else:
                p += 1

            if j < n-1 and graph[i][j+1] == "#":
                if not visited[i][j+1]:
                    queue.append((i, j+1))
            else:
                p += 1
    # print("area, perimeter", a, p)
    return a, p

m_area = 0
m_perimeter = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            if graph[x][y] == "#":
                area, perimeter = flood(x, y)
                if area > m_area:
                    m_area = area
                    m_perimeter = perimeter
                elif area == m_area:
                    m_area = m_area if m_perimeter < perimeter else area
                    m_perimeter = min(m_perimeter, perimeter)
            visited[x][y] = True
      
# print(m_area, m_perimeter)
fout.write(str(m_area) + " " + str(m_perimeter))
fout.close