n, m = map(int, input().split())
lis = [[i+1 for i in range(n) if i != j] for j in range(n)]
for i in range(m):
    A = list(map(int, input().split()))
    for j in range(1, A[0]):
        key = A[j]
        for other in A[j:]:
            if other in lis[key-1]:
                ind = lis[key-1].index(other)
                lis[key-1].pop(ind)
            if key in lis[other-1]:
                ind = lis[other-1].index(key)
                lis[other-1].pop(ind)

count = 0
for i in lis:
    count += sum(i)
if count == 0:
    print("Yes")
else:
    print("No")