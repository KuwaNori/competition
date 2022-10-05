n = int(input())
l = []
result = "Yes"
for i in range(n):
    s,m = input().split()
    if s not in l:
        l.append(s)
        if m not in l:
            l.append(m)
        else:
            result = "No"
print(result)
