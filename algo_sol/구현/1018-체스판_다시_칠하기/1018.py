n,m = map(int,input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        result1 = 0
        result2 = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) %2 == 0:
                    if board[x][y] != 'B':
                        result1 += 1
                    if board[x][y] != 'W':
                        result2 += 1
                else:
                    if board[x][y] != 'W':
                        result1 += 1
                    if board[x][y] != 'B':
                        result2 += 1
        result.append(result1)
        result.append(result2)

print(min(result))