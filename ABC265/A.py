import math

x, y, n = map(int, input().split())
if min(x*3, y) == y:
    result = math.floor(n / 3) * x + (n % 3) * y
else:
    result = n*x
print(result)