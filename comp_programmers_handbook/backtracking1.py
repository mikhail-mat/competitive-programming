chessboard = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
n = len(chessboard)

column = [0,0,0,0]
diag1 = [0,0,0,0,0,0,0]
diag2 = [0,0,0,0,0,0,0]

count = 0

def search(y):
    global count
    if y == n:
        count += 1
        return None
    else:
        for x in range(len(chessboard[y])):
            if column[x] or diag1[x+y] or diag2[x-y+n-1]: continue
            column[x] = diag1[x+y] = diag2[x-y+n-1] = 1
            search(y+1)
            column[x] = diag1[x+y] = diag2[x-y+n-1] = 0

search(0)
print(count)
