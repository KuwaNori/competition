# from 11:15 end 11:
# イコールになるパターンと
# Cが偶数と奇数のパターンの3つをつくり
# その中で偶数なら絶対値で比較し、奇数ならそのまま比較シてACできた
a, b, c = map(int, input().split())
if (a == 0 and b == 0) or a == b or c == 0:
    print("=")
elif c%2 == 0:
    if abs(a) == abs(b): print("=")
    elif abs(a) > abs(b): print(">")
    else: print("<")
else:
    if a > b: print(">")
    else: print("<")
