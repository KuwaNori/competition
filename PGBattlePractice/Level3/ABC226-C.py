n = int(input())
INF = float('inf')
l = [INF for i in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    t, k = line[0], line[1]
    if k >= 1: s = sum([l[i-1] for i in line[2:k+2]]) + t
    else: s = t
    l[i] = s
print(l[-1])
