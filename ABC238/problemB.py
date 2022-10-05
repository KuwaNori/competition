n = int(input())
A = list(map(int,input().split()))
c = [0,360]
l = 0
for a in A:
    k = l + a
    c.append(k%360)
    l = k
s = sorted(c)
g = 0
for i in range(1,len(s)):
    t = s[i] -  s[i-1]
    if t > g:
        g = t
print(g)
    
