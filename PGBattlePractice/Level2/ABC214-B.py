# from 22:00 - 22:13
# 学んだこと

s, t = map(int, input().split())
count = 0
n = s + 1
for a in range(0, n):
    for b in range(0, n):
        for c in range(0, n):
            if a + b + c <= s and a * b * c <= t:
                count += 1
print(count)