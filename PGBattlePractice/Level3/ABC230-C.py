# from 19:55
# 学んだこと
# 基準を決めて計算量を落とす。
n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
field = [["." for _ in range(s-r+1)] for _ in range(q-p+1)]
x = max(p-a, r-b)
y = min(q-a, s-b)
for i in range(x, y+1):
    field[a + i -p][b + i - r] = "#"
x = max(p-a, b-s)
y = min(q-a, b-r)
for i in range(x, y+1):
    field[a + i - p][b - i - r] = "#"

for line in field:
    print("".join(line))
