# # """
# # ID: spencewert
# # LANG: PYTHON3.4.0
# # PROG: daisy
# # """

# # class Cow:
# #     def __init__(self, index):
# #         self.index = index
# #         self.positions = [index]
# from collections import defaultdict
# raw_inp = str(input()).split(" ")
# n, k = int(raw_inp[0]), int(raw_inp[1])
# # print(n, k)
# moves = []
# for _ in range(k):
#     r_inp = str(input()).split(" ")
#     a, b = int(r_inp[0]), int(r_inp[1])
#     moves.append((a-1, b-1))

# #print(moves)
# cows = [[f, [f]] for f in range(n)]
# for move in moves:
#     cows[move[0]][1].append(move[1])
#     cows[move[1]][1].append(move[0])
#     cows[move[0]], cows[move[1]] = cows[move[1]], cows[move[0]]
#     #print(move[0], move[1], "flipped")

# s_cows = sorted(cows, key=lambda x: x[0])
# #completed = [[] for _ in range(n)]
# #print(s_cows)

# dp = defaultdict(list)


# def find_links(visited, pos_list):
#     global dp, s_cows
#     #print ("pos list", pos_list)
#     if dp[pos_list[0]]:
#        # print("happens")
#         return dp[pos_list[0]]
#     if visited[pos_list[0]]:
#        # print("visited")
#         return s_cows[pos_list[0]][1]
#     visited[pos_list[0]] = True
#     links = find_links(visited, s_cows[pos_list[-1]][1])
#     #print("links", links)
#     #print("pos_list", pos_list)
#     dp[pos_list[0]] = pos_list + links
#    # print(dp[pos_list[0]])
#     return dp[pos_list[0]]

# for c in s_cows:
#     # last_visit = c[1][-1]
#     # completed[c[1][0]] = c[1]
#     # while completed[last_visit] != []:
#     #     c[1] = c[1] + s_cows[last_visit][1]
#     #     completed[last_visit] = c[1]
#     #     last_visit = c[1][-1]
#     l = find_links([False for _ in range(n)], c[1])
#     #print(l)
#     print(len(set(l)))


# """
# ID: spencewert
# LANG: PYTHON3.4.0
# PROG: daisy
# """

class Cow:
    def __init__(self, index):
        self.index = index
        self.positions = [index]

raw_inp = str(input()).split(" ")
n, k = int(raw_inp[0]), int(raw_inp[1])
# print(n, k)
moves = []
for _ in range(k):
    r_inp = str(input()).split(" ")
    a, b = int(r_inp[0]), int(r_inp[1])
    moves.append((a-1, b-1))

cows, nonswap = [], []
for x in range(n):
    cow = Cow(x)
    cows.append(cow)
    nonswap.append(cow)
#print(moves)
for move in moves:
    cows[move[0]].positions.append(move[1])
    cows[move[1]].positions.append(move[0])
    cows[move[0]], cows[move[1]] = cows[move[1]], cows[move[0]]
    #print(move[0], move[1], "flipped")

#s_cows = sorted(cows, key=lambda x: x.index)
completed = [False for _ in range(n)]
for c in nonswap:
    visited = [False for _ in range(n)]
    last_visit = c.positions[-1]
    while not visited[last_visit]:
        visited[last_visit] = True
        c.positions = c.positions + nonswap[last_visit].positions
        if completed[last_visit]:
            break
        last_visit = c.positions[-1]
    completed[c.index] = True
    print(len(set(c.positions)))
