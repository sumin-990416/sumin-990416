# 📝 Baekjoon 1261: 알고스팟

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-24 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `최단 경로` | [1261번 문제](https://www.acmicpc.net/problem/1261) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 다익스트라 알고리즘을 이용하여  `m x n` 크기의 격자에서 (0, 0) 위치에서 (m-1, n-1) 위치까지 이동하는 최소 비용을 구합니다. 각 셀에는 이동 비용이 주어지며, 상하좌우로만 이동할 수 있습니다.  `heapq` 모듈을 사용하여 우선순위 큐를 구현하여 효율적으로 최소 비용을 찾습니다.


### 📝 **알고리즘**

1. **초기화:** `money_sum` 이라는 2차원 배열을 생성하여 각 셀까지의 최소 비용을 저장합니다. 처음에는 모든 값을 무한대로 초기화하고, 출발점 (0, 0)의 비용은 0으로 설정합니다. 우선순위 큐 `prior`를 생성하고, 출발점의 비용과 좌표를 삽입합니다.

2. **다익스트라 알고리즘:** 우선순위 큐에서 최소 비용을 가지는 셀을 꺼냅니다.  이미 방문한 셀보다 비용이 크다면 건너뜁니다.

3. **인접 셀 탐색:** 현재 셀의 상하좌우 인접 셀을 탐색합니다. 인접 셀의 새로운 비용을 계산하고, 기존에 저장된 최소 비용보다 작다면 `money_sum` 배열을 갱신하고, 새로운 비용과 좌표를 우선순위 큐에 추가합니다.

4. **종료 조건:** 우선순위 큐가 비어있으면 알고리즘을 종료하고, 목표 지점 (m-1, n-1) 까지의 최소 비용을 반환합니다.


### 🧐 **시간 복잡도**

다익스트라 알고리즘은 우선순위 큐를 사용하여 구현되었으므로, 최악의 경우 모든 셀을 방문하게 되어 시간 복잡도는 O(E log V) 입니다. 여기서 V는 셀의 개수 (m*n), E는 간선의 개수 (최대 4*m*n) 이므로, 시간 복잡도는 O(mn log(mn)) 입니다.  `heapq` 모듈은 파이썬의 기본 제공 우선순위 큐 구현체로 로그 시간 복잡도를 가집니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1261: 알고스팟
# https://www.acmicpc.net/problem/1261

import heapq

def dijkstra():
    money_sum = [[float('inf')]*n for _ in range(m)]
    money_sum[0][0] = 0
    prior =[]

    heapq.heappush(prior, (arr[0][0],0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while prior:
        money, x, y = heapq.heappop(prior)

        if money > money_sum[y][x]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m:
                new_money = money + arr[ny][nx]

                if new_money < money_sum[ny][nx]:
                    money_sum[ny][nx] = new_money
                    heapq.heappush(prior,(new_money,nx,ny))
    return money_sum[-1][-1]



n, m = map(int,input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int,input())))
print(dijkstra())
</details>