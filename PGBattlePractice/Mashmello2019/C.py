n, m = map(int, input().split())
l = [1 for _ in range(m)]
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if i - (a+b-1) < 0 or i - (a+b-1) > m:
        continue
    elif l[i-(a+b)] == 1:
        ans+=1
        l[i-(a+b)] = 0
print(ans)
