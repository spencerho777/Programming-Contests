"""
ID: spencew2
LANG: PYTHON3
PROG: beads
"""


#fin = open("beads.in", 'r')
fout = open("beads.out", 'w')
fout.truncate(0)

metadata =  "29"#str(fin.readline().strip())
inp = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb"#str(fin.readline().strip())

num_beads = int(metadata)
bead_c = []
count = 0

for i in range(num_beads):
    if inp[i] != 'w':
        last = inp[i]
        break
for i in range(0, num_beads):
    print(inp[i])
    if inp[i] == "w":
        bead_c.append('w')
        continue
    elif inp[i] == last:
        count += 1
    else:
        bead_c.append(count)
        count = 1
    last = inp[i]


m = 0

print(bead_c)
print(m)
fout.write(str(m))
fout.close()