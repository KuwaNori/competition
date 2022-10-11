def getPattern(m):
    l = [i ** 2 for i in range(100)]
    for i in l:
        for j in l:
            if i + j == m:
                if i == 0: a = 0
                else: a = i // i
                if j == 0: b = 0
                else: b = j // j
                return [a, b]
    return None


# x,y is gap, i,j is current position
def getChangeList(i, j, x, y, field):
    l = [[i + x, j + y], [i + y, j + x], [i - x, j - y], [i - y, j - x], [i + x, j - y], [i + y, j - x], [i + x, j - y],
         [i - y, j + x]]
    for pos in l:
        if pos[0] < 0 or pos[0] > n-1 or pos[1] < 0 or pos[1] > n -1:
            return field
        elif field[pos[0]][pos[1]] + 1 > field[i][j]:
            field[pos[0]][pos[1]] = field[i][j] + 1
            getChangeList(pos[0], pos[1], x, y, field)
        else:
            return field


n, m = map(int, input().split())
field = [[1000001 for _ in range(n)] for _ in range(n)]
field[0][0] = 0
result = getPattern(m)
if len(result) == 0:
    for i in range(n):
        for j in range(n):
            print(-1, end="")
        print()
else:
    ans = getChangeList(0, 0, result[0], result[1], field)
    for line in ans:
        print("".join(map(str, line)))
