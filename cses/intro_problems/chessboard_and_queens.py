chessboard = []
for i in range(8):
    chessboard.append(input())

column = [0 for i in range(8)]
diag1 = [0 for i in range(15)]
diag2 = [0 for i in range(15)]

count = 0

def search(y):
    global count
    if y == 8:
        count += 1
        return None
    else:
        for x in range(8):
            if chessboard[y][x] == '*': continue
            if column[x] or diag1[x+y] or diag2[x-y+7]: continue
            column[x] = diag1[x+y] = diag2[x-y+7] = 1
            search(y+1)
            column[x] = diag1[x+y] = diag2[x-y+7] = 0

search(0)
print(count)
