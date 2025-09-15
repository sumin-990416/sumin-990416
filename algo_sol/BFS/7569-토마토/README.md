# 📝 Baekjoon 7569: 토마토

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![골드 5](https://img.shields.io/badge/Gold-5-E5A323?style=for-the-badge) | `BFS` | [7569번 문제](https://www.acmicpc.net/problem/7569) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

3차원 배열에서 1로 표시된 토마토들이 인접한 0인 토마토들을 익게 하는 과정을 BFS(Breadth-First Search) 알고리즘으로 모델링합니다.  BFS를 통해 모든 토마토가 익을 때까지 걸리는 최소 일수를 계산합니다. 만약 모든 토마토가 익을 수 없는 경우 -1을 반환합니다.  토마토가 익는 데 걸리는 날짜는 익은 토마토의 값 + 1 로 계산됩니다.


### 📝 **알고리즘**

1. **입력:**  토마토의 3차원 배열 `arr_all`을 입력받습니다.  `n`은 높이, `m`은 가로, `k`는 세로 크기를 나타냅니다.
2. **초기화:** 익은 토마토(`arr_all[z][x][y] == 1`)의 위치를 큐 `totato`에 저장합니다.
3. **BFS:** `totato` 큐를 이용하여 BFS를 수행합니다.  큐에서 익은 토마토의 위치를 하나씩 꺼내 인접한 익지 않은 토마토(`arr_all[nz][nx][ny] == 0`)의 값을 현재 토마토의 값 + 1로 업데이트하고, 큐에 추가합니다.
4. **결과 확인:** BFS가 완료된 후, 모든 토마토가 익었는지 확인합니다.  만약 0이 남아있다면 -1을 반환하고, 그렇지 않다면 최대 일수(최대값 -1)를 반환합니다.

### 🧐 **시간 복잡도**

BFS 알고리즘을 사용하므로, 최악의 경우 모든 토마토를 방문해야 합니다.  3차원 배열의 크기가 n x m x k 이므로 시간 복잡도는 O(nmk)입니다.  큐에 대한 연산(enqueue, dequeue)은 상수 시간에 이루어지므로 전체적인 시간 복잡도에 영향을 미치지 않습니다.  마지막으로 모든 토마토를 확인하는 부분도 O(nmk)의 시간 복잡도를 가지므로, 전체 알고리즘의 시간 복잡도는 O(nmk) 입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 7569: 토마토
# https://www.acmicpc.net/problem/7569

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
</details>