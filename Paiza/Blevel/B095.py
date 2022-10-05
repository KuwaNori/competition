N, M = map(int, input().split())
correct = []
scores = [100 for i in range(N)]
for i in range(M):
    correct.append(int(input()))

for i in range(N):
    for correct_note in correct:
        diff = abs(correct_note - int(input()))
        if diff <= 5:
            continue
        elif diff <= 10:
            scores[i] -= 1
        elif diff <= 20:
            scores[i] -= 2
        elif diff <= 30:
            scores[i] -= 3
        else:
            scores[i] -= 5
    if scores[i] < 0:
        scores[i] = 0
print(max(scores))