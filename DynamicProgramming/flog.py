N = int(input())
poles = list(map(int, input().split()))
dp = [100 for _ in range(N)]
dp[0] = 0
dp[1] = abs(poles[0] - poles[1])
for i in range(2, N):
    dp[i] = min(dp[i - 2] + abs(poles[i] - poles[i - 2]), dp[i - 1] + abs(poles[i] - poles[i - 1]))
print(dp[-1])
