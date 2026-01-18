import string

word = input()
score = 0
for char in word:
    score += ord(char) - 64

"""
RECURSIVE
"""

# memo = {0: ['']}

# def find_words(score):
#     if score in memo: return memo[score]
#     memo[score] = []
#     for let in string.ascii_uppercase:
#         let_score = ord(let) - 64
#         if let_score > score: break
#         for w in find_words(score-let_score):
#             if w == '' or let != w[0]:
#                 memo[score].append(let + w)
#     return memo[score]

# print(find_words(score).index(word)+1)

"""
ITERATIVE
"""

# dp = [[] for i in range(score+1)]
# dp[0] = ['']

# for i in range(1, score+1):
#     for let in string.ascii_uppercase:
#         let_score = ord(let) - 64
#         if let_score > i: break
#         for w in dp[i-let_score]:
#             if w == '' or let != w[0]:
#                 dp[i].append(let + w)

# print(dp[score].index(word)+1)

dp = [[0] * 27 for i in range(score+1)]
dp[0][0] = 1

for i in range(1, score+1):
    for let in string.ascii_uppercase:
        let_score = ord(let) - 64
        if let_score > i: break
        for j in range(27):
            if let_score == j: continue
            dp[i][let_score] += dp[i-let_score][j]

print(dp)
