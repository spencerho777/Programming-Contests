"""
ID: spencewert
LANG: PYTHON3.4.0
PROG: triangles
"""
import itertools
fin = open("triangles.in", 'r')
fout = open("triangles.out", 'w')

num_fences = int(fin.readline())
posts = []#[]

for _ in range(num_fences):
    post = str(fin.readline().strip()).split(" ")
    x, y = int(post[0]), int(post[1])
    posts.append((x, y))
def dif(pt1, pt2):
    return max(abs(pt2[0]-pt1[0]), abs(pt2[1]-pt1[1]))
combinations = itertools.combinations(posts, 3)
#print(list(combinations))
m_area = 0
for c in combinations:
    s = sorted(c, key=lambda x: (abs(x[0]), abs(x[1])))
    t1, t2, t3 = c[0], c[1], c[2]
    if (t1[0] == t2[0] or t1[0] == t3[0] or t2[0] == t3[0]):
        if (t1[1] == t2[1] or t1[1] == t3[1] or t2[1] == t3[1]):
            a = dif(t2, t1) * dif(t3, t1)
            #print(t1, t2, t3, a)
            #print(dif(t2, t1), dif(t3, t1))
            if m_area < a:
                print(s)
                m_area = a
fout.write(str(int(m_area)))
fout.close()

