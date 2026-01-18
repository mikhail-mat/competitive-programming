import sys

data = list(map(int, sys.stdin.read().split()))
n, x = data[0], data[1]
c = sorted(data[2:2+n])

MOD = 10**9 + 7
dp = [0] * (x+1)
dp[0] = 1

for i in range(1, x+1):
    s = 0
    for coin in c:
        if coin > i: break
        s += dp[i - coin]
    if s >= MOD: s %= MOD
    dp[i] = s

print(dp[x])
