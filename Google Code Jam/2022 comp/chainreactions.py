
class Node:
    def __init__(self, value):
        self.value = value
        self.children = set()
        self.visited = False

class Tree:
    root = None
    def __init__(self, root):
        self.root = root

t = int(input())

def solve(n, modules, pointers):
    trees = []
    nodes = [Node(modules[x]) for x in range(n)]
    for p in range(len(pointers)):
        if pointers[p] == 0:
            trees.append(nodes[p])
        else:
            nodes[pointers[p]].children.add(p=====)
    print_all_nodes(nodes)
    # dfs

    for tree in trees:
        stack = [tree.root]
        
        while stack:
            if len(stack[0].children) != 0:
                stack.append()
            

    
    return "IMPOSSIBLE"

s = 0
def dfs(root):
    if len(root.children) != 0:
        options = []
        for child in root.children:
            options.append(dfs(child))
            


    return None


def print_all_nodes(nodes):
    for i in range(len(nodes)):
        print(i, nodes[i].value, nodes[i].adj)



for case in range(1, t+1):
    n = int(input())
    modules = [int(x) for x in str(input()).split(" ")]
    pointers = [int(x) for x in str(input()).split(" ")]

    print("Case #" + str(case) + ": " + solve(n, modules, pointers))