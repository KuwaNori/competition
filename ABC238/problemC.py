def getNum(n):
    return n

A = list(input())
N = int(input())
r = 0
for i in range(10,N+1):
    print(i)
    r+=i-9999
print(r)


print(r%998244353)
