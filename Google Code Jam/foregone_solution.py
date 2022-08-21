
def find_4(string):
    string = string[::-1]
    indexes = []
    for c in range(len(string)):
        if string[c] == "4":
            indexes.append(c)
    return indexes

def replace_4():
    num = int(input())
    index = find_4(str(num))
    res = 0
    for n in index:
        res += 10 ** n
    num -= res
        
    return "%s %s" % (num, res)
    

for case in range(int(input())):
    answer = replace_4()
    print("Case #{}: {}".format( case + 1, answer ))
