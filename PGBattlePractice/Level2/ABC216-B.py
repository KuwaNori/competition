n = int(input())
l = []
ans = "No"
for i in range(n):
    k = list(input().split())
    if k in l:
        ans = "Yes"
    else:
        l.append(k)
print(ans)