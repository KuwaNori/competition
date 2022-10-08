n = int(input())
A = list(map(int, input().split()))
odd1, odd2, even1, even2 = 0,0,0,0
for k in A:
    if k%2 == 1:
        if k > odd1:
            odd2 = odd1
            odd1 = k
        elif k > odd2:
            odd2 = k
    else:
        if k > even1:
            even2 = even1
            even1 = k
        elif k > even2:
            even2 = k
if odd2 == 0 and even2 == 0:
    if odd1 == 0 and even1 == 0:
        print(0)
    else:
        print(-1)
else:
    print(max((odd1+odd2),(even1+even2)))