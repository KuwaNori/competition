# from 8:07 end 8:11
n = int(input())
A = list(map(int, input().split()))
total = 0
for i in A:
    if i < 10:
        continue
    else:
        total += i - 10
print(total)
