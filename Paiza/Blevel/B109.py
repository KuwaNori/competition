# 映画館の席の予約
N, H, W, P, Q = map(int, input().split())
field = [[abs(P-h)+abs(Q-w) for w in range(W)] for h in range(H)]
for i in range(N):
    p, q = map(int, input().split())
    field[p][q] = 100000
bottom = 100000
for line in field:
    l = min(line)
    if bottom > l:
        bottom = l
minlist = []
for p in range(H):
    for q in range(W):
        if field[p][q] == bottom:
            minlist.append([p,q])
for cell in minlist:
    print(str(cell[0]) + " " + str(cell[1]))




