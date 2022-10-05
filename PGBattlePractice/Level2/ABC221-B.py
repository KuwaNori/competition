# 学んだこと
# 一部を入れ替えた除隊で比べて一致すれば複数ヶ所を調べる必要がなくなる
# 8行目、12行目のように入れ替えを一行で表現すれば仮の箱を用意せずに済む
s = list(input())
t = list(input())
ans = "No"
for i in range(len(s)-1):
    s[i], s[i+1] = s[i+1], s[i]
    print("".join(s))
    if s == t:
        ans = "Yes"
    s[i], s[i+1] = s[i+1], s[i]
print(ans)


# flag, count = 0, 0
# for i in range(len(s)):
#     if flag == 0 and s[i] != t[i]:
#         M, F = s[i], t[i]
#         count += 1
#         flag = 1
#     elif flag == 1 and M != t[i] and F != s[i]:
#         count += 2
#         flag = 0
# if count <= 1:
#     print("Yes")
# else:
#     print("No")
