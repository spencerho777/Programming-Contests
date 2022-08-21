

n = int(input())

def solve(r, c):

    be = ".." + ("+-" * (c - 1)) + "+"
    print(be)

    second = ".." + ("|." * (c - 1)) + "|"
    print(second)

    lb = ("+-" * c) + "+"
    for _ in range(r-1):
        print(lb)
        print(("|." * (c)) + "|")
    print(lb)


for case in range(n):
    inp = str(input()).split(" ")
    r, c = int(inp[0]), int(inp[1])
    print("Case #" + str(case+1) + ":")
    solve(r, c)