# 📝 Baekjoon 4485: 녹색 옷 입은 애가 젤다지

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-24 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `최단 경로` | [4485번 문제](https://www.acmicpc.net/problem/4485) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 다익스트라 알고리즘을 이용하여 NxN 크기의 격자에서 (0, 0) 지점부터 (N-1, N-1) 지점까지 이동하는 최소 비용을 구합니다.  각 칸에는 이동 비용이 주어지며, 상하좌우로 인접한 칸으로만 이동할 수 있습니다. 최소 비용을 찾기 위해 우선순위 큐(힙)을 사용하여 효율적으로 탐색합니다.


### 📝 **알고리즘**

1. **초기화:**  `money_sum` 2차원 리스트는 각 칸에 도달하는 최소 비용을 저장합니다.  모든 칸의 초기 비용은 무한대로 설정됩니다. 우선순위 큐 `prior`에는 (비용, x좌표, y좌표) 튜플을 저장합니다. (0, 0) 지점부터 시작하므로, (arr[0][0], 0, 0)을 큐에 추가합니다.

2. **다익스트라 알고리즘:** 우선순위 큐가 빌 때까지 반복합니다.
   - 큐에서 가장 비용이 적은 (money, x, y)를 꺼냅니다.
   - 만약 현재 비용 `money`가 `money_sum[x][y]`보다 크다면, 이미 더 짧은 경로가 발견되었으므로 해당 노드는 무시합니다.
   - 상하좌우 인접한 칸들을 탐색합니다.
   - 인접 칸 (nx, ny)에 대한 새로운 비용 `new_money`를 계산합니다.
   - 만약 `new_money`가 `money_sum[nx][ny]`보다 작다면, 더 짧은 경로가 발견된 것이므로 `money_sum[nx][ny]`를 갱신하고, (new_money, nx, ny)를 우선순위 큐에 추가합니다.

3. **결과 반환:** 반복문이 끝난 후, `money_sum[-1][-1]` (즉, (N-1, N-1) 칸의 최소 비용)을 반환합니다.


### 🧐 **시간 복잡도**

다익스트라 알고리즘은 우선순위 큐를 사용하여 구현되었으므로, 최악의 경우 모든 칸을 방문하게 됩니다.  각 칸은 최대 4번 우선순위 큐에 추가될 수 있으며, 우선순위 큐의 삽입 및 삭제 연산은 O(log N²)의 시간이 걸립니다 (N²은 전체 칸의 수). 따라서 전체 시간 복잡도는 O(N² log N²) 입니다.  힙을 사용한 다익스트라 알고리즘의 일반적인 시간 복잡도와 일치합니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 4485: 녹색 옷 입은 애가 젤다지
# https://www.acmicpc.net/problem/4485

import heapq

def dijkstra():
    money_sum = [[float('inf')]*n for _ in range(n)]

    prior =[]

    heapq.heappush(prior, (arr[0][0],0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while prior:
        money, x, y = heapq.heappop(prior)

        if money > money_sum[x][y]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n:
                new_money = money + arr[nx][ny]

                if new_money < money_sum[nx][ny]:
                    money_sum[nx][ny] = new_money
                    heapq.heappush(prior,(new_money,nx,ny))
    return money_sum[-1][-1]



i = 1
while True:
    n = int(input())
    if n == 0:
        break

    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    print(f'Problem {i}: {dijkstra()}')
    i += 1
</details>