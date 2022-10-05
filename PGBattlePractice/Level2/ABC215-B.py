import math
n = int(input())
count = 0
# while True:
#     if n <= 1:
#         break
#     n = math.floor(n/2)
#     count+=1
# print(count)

while True:
    if 2**count > n:
        count-=1
        break
    count+=1
print(count)