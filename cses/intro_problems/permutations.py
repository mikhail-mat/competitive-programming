import sys

input = sys.stdin.readline
n = int(input())

res = []

if 1 < n < 4:
    print('NO SOLUTION')
else:
    for i in range(2, n + 1, 2):
        res.append(str(i))
    for i in range(1, n + 1, 2):
        res.append(str(i))

sys.stdout.write(' '.join(res) + "\n")
