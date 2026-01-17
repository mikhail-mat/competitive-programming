n = int(input())

"""
RECURSION DP
"""

# count = {0: 1}
# def dice_combos(n):
#     if n in count: return count[n]
#     count[n] = 0
#     for i in range(1, 7):
#         if n - i >= 0:
#             count[n] += dice_combos(n-i) % (10**9 + 7)
#     return count[n]

# print(dice_combos(n))

"""
ITERATIVE DP
"""

dp = [0] * (n+1) # init array to store values for each sum
dp[0] = 1 # base case sum = 0 -> 1

for i in range(1, n+1): # loop through possible sums (build from bottom up)
    for dice in range(1, 7): # loop through previous 6 sums
        if i - dice >= 0:
            dp[i] = (dp[i] + dp[i-dice]) % (10**9 + 7) # add previous sum

print(dp[n])
