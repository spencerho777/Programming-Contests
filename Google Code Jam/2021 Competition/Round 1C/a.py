
def computate(n, k, inp):
    s_list = sorted(set(inp))
    #print(s_list)
    dist = []
    for i in range(len(s_list)-1):
        between = (s_list[i+1] - s_list[i] - 1)
        ans = between // 2
        if between % 2 == 1:
            ans += 1
        dist.append(ans)
        dist.append(between - ans)
    
    if s_list[0] != 1:
        dist.append(s_list[0]-1)
    if s_list[-1] != k:
        dist.append(k - s_list[-1])
    dist.sort(reverse=True)
    #print(dist)
    if dist == []:
        return 0.0
    if len(dist) == 1:
        return dist[0]/k
    return (dist[0] + dist[1])/k
for case in range(int(input())):
    r_inp = str(input()).split(" ")
    n, k = r_inp[0], int(r_inp[1])
    inp = [int(a) for a in str(input()).split(" ")]
    answer = computate(n, k, inp)
    print("Case #{}: {}".format( case + 1, answer ))
