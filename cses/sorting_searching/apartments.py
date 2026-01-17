n, m, k = map(int, input().split())
des_sizes = list(map(int, input().split()))
sizes = list(map(int, input().split()))

# 10 10 10
# 90 41 20 39 49 21 35 31 74 86
# 14 24 24 7 82 85 82 4 60 95

# 20 21 31 35 39 41 49 74 86 90
# 4 7 14 24 24 60 82 82 85 95

des_sizes.sort()
sizes.sort()

res = 0

i = j = 0
while i < len(des_sizes) and j < len(sizes):
    if sizes[j] < des_sizes[i]:
        if des_sizes[i] - sizes[j] <= k:
            res += 1
            i += 1
            j += 1
        else:
            j += 1
    else:
        if sizes[j] - des_sizes[i] <= k:
            res += 1
            i += 1
            j += 1
        else:
            i += 1

print(res)
