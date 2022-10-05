# from 22:16 end 10:35
# 見直しをシましょう
n = int(input())
A = list(map(int, input().split()))
if A[0] > A[1]:
    boo, biri = 1, 0
else:
    boo, biri = 0, 1
if n < 2:
    print(boo+1)
else:
    for i in range(2, n):
        if A[i] > A[boo]:
            if A[i] > A[biri]:
                boo = biri
                biri = i
            else:
                boo = i
    print(boo+1)