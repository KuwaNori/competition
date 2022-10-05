# 学んだこと
# 文字列にmin,maxを使うことが可能
s = input()
n = len(s)
v = []
for k in range(n):
    v.append(s[k:n] + s[0:k])
print(min(v))
print(max(v))