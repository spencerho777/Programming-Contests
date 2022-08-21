"""
ID: spencewert
LANG: PYTHON3.4.0
PROG: socdist1
"""

#FAILED CASE 3, 5, 6. 12/15

fin = open("socdist1.in", 'r')
fout = open("socdist1.out", 'w')

num_stalls = int(fin.readline())
stall_layout = str(fin.readline().strip())


#stall_layout = "00000001000"
#num_stalls = len(stall_layout)

empties = []
start_cow = False
running = 0
e1, e2 = 0, 0
for char in range(num_stalls):
    #print(char)
    if stall_layout[char] == "1":
        if start_cow:
            if running > e1 or running > e2:
                if min(e1, e2) == e1:
                    if e1 == 0:
                        e1 = running
                    else:
                        e1 = running
                else:
                    e2 = running
            if char != 0:
                empties.append(running+1)
            running = 0
        else:
            start_cow = True
            e1 = running
    else:
        running += 1

        
if running > e1 or running > e2:
    if min(e1, e2) == e1:
        e1 = running
    else:
        e2 = running

e1Max = max(e1, e2) == e1
e1+=1
e2+=1
min_e = min(empties) if empties != [] else float('inf')
print(e1, e2, min_e)

if ((e1 // 3) > (e2 // 2)):
    min_a = e1//3
    print("e1//3", e1//3)
elif ((e2 // 3) > (e1 // 2)):
    min_a = e2//3
    print("e2//3", e2//3)
else:
    min_a = min(e1, e2) // 2
    print(min(e1, e2) // 2)

if min_e < min_a:
    fout.write(str(min_e))
else:
    if min_a == 0:
        min_a = 1
    fout.write(str(min_a))
print(min(min_e, min_a))
fout.close()


