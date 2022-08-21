
for case in range(int(input())):
    maze_size= int(input())
    lydia = str(input())
    me = []
    for c in range(len(lydia)):
        if lydia[c] == "E":
            me.append("S")
        else:
            me.append("E")

    print("Case #{}: {}".format(case + 1, ''.join(me)))
