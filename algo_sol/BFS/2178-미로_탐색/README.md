# 📝 Baekjoon 2178: 미로 탐색

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![실버 1](https://img.shields.io/badge/Silver-1-949393?style=for-the-badge) | `BFS` | [2178번 문제](https://www.acmicpc.net/problem/2178) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 BFS(Breadth-First Search, 너비 우선 탐색) 알고리즘을 이용하여 미로의 시작점에서 끝점까지의 최단 경로 길이를 구합니다.  `node` 딕셔너리를 이용하여 각 셀과 연결된 인접 셀들을 미리 저장해 효율적으로 탐색합니다.  방문 여부를 `visited` 배열로 관리하여 중복 탐색을 방지합니다.

### 📝 **알고리즘**

1. **입력:** 미로의 크기(n, m)와 미로 정보(arr)를 입력받습니다.
2. **그래프 생성:**  미로 정보를 기반으로 각 셀(i, j)과 연결된 인접 셀들을 `node` 딕셔너리에 저장합니다.  인접 셀은 상하좌우 4방향으로 1(길)인 셀들입니다.
3. **BFS 탐색:** `deque`를 이용하여 BFS를 수행합니다. 시작점 (0, 0)에서 시작하여 큐에 (x, y, num) 튜플을 저장합니다.  여기서 x, y는 현재 위치, num은 시작점부터 현재 위치까지의 거리입니다.
4. **방문 처리:**  큐에서 꺼낸 셀 (x, y)가 방문하지 않았다면 `visited[x][y]`를 True로 설정하고, 인접 셀들을 탐색합니다.
5. **목표 지점 확인:** 인접 셀 중 끝점 (n-1, m-1)이 있다면, 시작점부터 끝점까지의 거리 num + 1을 반환합니다.
6. **큐에 추가:**  끝점이 아니라면 인접 셀을 큐에 추가합니다.
7. **결과 출력:** BFS 탐색이 완료되면 시작점에서 끝점까지의 최단 거리를 출력합니다.


### 🧐 **시간 복잡도**

- 그래프 생성: O(n*m) - 미로의 모든 셀을 한 번씩 방문하여 인접 셀을 확인합니다.
- BFS 탐색: 최악의 경우 모든 셀을 방문하므로 O(n*m)입니다.

따라서 전체 시간 복잡도는 O(n*m)입니다.  공간 복잡도 또한 O(n*m)입니다.  `visited` 배열과 `node` 딕셔너리가 미로의 크기에 비례하는 공간을 사용하기 때문입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 2178: 미로 탐색
# https://www.acmicpc.net/problem/2178

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
</details>