n = int(input())
INF = float('inf')
l = [INF for i in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    t, k = line[0], line[1]
    if k >= 1: s = l[line[-1]-1] + t
    else: s = t
    l[i] = s
print(l)
print(l[-1])
