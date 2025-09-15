from collections import deque
def maze(start,end,cnt):
    stack = deque([(start,end,cnt)])
    while stack:
        x,y,num= stack.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for new_x,new_y in node[(x,y)]:
                if new_x == n-1 and new_y == m-1:
                    return num+1
                else:
                    stack.append((new_x,new_y,num+1))



n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

node = {}
for i in range(n):
    for j in range(m):
        node[(i,j)] = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if arr[nx][ny] == 1:
                        node[(i,j)].append((nx,ny))
                        node[(nx,ny)].append((i,j))


visited = [[False] * m for _ in range(n)]

print(maze(0,0,1))