import sys
input = sys.stdin.readline

n, x = map(int, input().split())
c = list(map(int, input().split()))

INF = 10**9
dp = [INF] * (x+1)
dp[0] = 0

for coin in c:
    for i in range(coin, x+1):
        val = dp[i-coin] + 1
        if val < dp[i]:
            dp[i] = val

ans = dp[x]
sys.stdout.write(str(-1 if ans == INF else ans))
