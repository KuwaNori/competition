N, M = map(int, input().split())
cant = []
for j in range(N):
    line = list(map(int, input().split()))
    for i in range(N):
        if line[i] >= M:
            cant.append(i+1)
result = [i + 1 for i in range(N)]
for i in set(cant):
    result.remove(i)
if len(result) == 0:
    print("wait")
else:
    print(" ".join(map(str, result)))
