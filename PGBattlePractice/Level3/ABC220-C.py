# from 21:58
import math

n = int(input())
A = list(map(int, input().split()))
x = int(input())
total = sum(A)
total2, count, base = 0, 0, 0
base = x//total
left = x - total * base

for i in A:
    total2 += i
    count += 1
    if total2 > left:
        break
print(count + (n * base))

