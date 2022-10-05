# 観覧車の稼働状況
N, M = map(int, input().split())
capacity = []
group = []
result = [0 for i in range(N)]
for i in range(N):
    capacity.append(int(input()))
for i in range(M):
    group.append(int(input()))
group_no = 0
cart_no = 0
number = 0
while True:
    if sum(group) == 0:
        break
    number = group[group_no]
    if group[group_no] - capacity[cart_no] <= 0:
        group[group_no] = 0
        result[cart_no] += number
    else:
        group[group_no] = group[group_no] - capacity[cart_no]
        result[cart_no] += capacity[cart_no]
    if group[group_no] == 0:
        group_no += 1
    if cart_no == N - 1:
        cart_no = 0
    else:
        cart_no += 1
    number = 0
for i in result:
    print(i)
