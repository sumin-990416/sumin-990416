from collections import deque

n,m,k = map(int,input().split())

arr_all = []
for _ in range(k):
    arr = []
    for _ in range(m):
        arr.append(list(map(int,input().split())))
    arr_all.append(arr)


totato = deque([])
for x in range(m):
    for y in range(n):
        for z in range(k):
            if arr_all[z][x][y] == 1:
                totato.append((x,y,z))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def make_totato(tt):
    while tt:
        x_1,y_1,z_1 = tt.popleft()
        for i in range(6):
            nx = x_1 + dx[i]
            ny = y_1 + dy[i]
            nz = z_1 + dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<k:
                if arr_all[nz][nx][ny] == 0:
                    arr_all[nz][nx][ny] += arr_all[z_1][x_1][y_1]+1
                    tt.append((nx,ny,nz))


    num = 0
    for i in range(len(arr_all)):
        for j in range(len(arr_all[i])):
            if 0 in arr_all[i][j]:
                return -1
            if max(arr_all[i][j]) > num:
                num = max(arr_all[i][j])
    return num-1

print(make_totato(totato))