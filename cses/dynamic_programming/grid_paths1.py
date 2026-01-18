import sys
input = sys.stdin.readline

n = int(input())
grid = []
for i in range(n):
    grid.append(input())

if grid[0][0] == '*':
    print(0)
else:
    MOD = 10**9 + 7
    dp = [[0] * n for i in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*': continue
            if i != 0:
                dp[i][j] += dp[i-1][j]
            if j != 0:
                dp[i][j] += dp[i][j-1]
            if dp[i][j] >= MOD:
                dp[i][j] %= MOD

    print(dp[n-1][n-1])
