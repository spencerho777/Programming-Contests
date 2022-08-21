
test = open("sample.in.txt", "r")

def get_input():
    return test.readline()#return input()

def solve(u_bound):
    print(u_bound)
    
    return "null"


for case in range(int(get_input())):
    u_bound = int(get_input())
    result = solve(u_bound)
    print("Case #{}: {}".format( case + 1, result ))
