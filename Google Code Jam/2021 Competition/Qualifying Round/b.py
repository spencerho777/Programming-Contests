
def computate(x, y, inp):
    last_letter = inp[0]
    cost = 0
    for i in range(1, len(inp)):
        #print(last_letter, inp[i])
        if inp[i] == "C":
            if last_letter == "J":
                cost += y
            last_letter = "C"
        elif inp[i] == "J":
            if last_letter == "C":
                cost += x
            last_letter = "J"

    return cost
            


for case in range(int(input())):
    inp = str(input()).split(" ")
    x, y, string = int(inp[0]), int(inp[1]), inp[2]
    answer = computate(x, y, string)
    print("Case #{}: {}".format( case + 1, answer ))
