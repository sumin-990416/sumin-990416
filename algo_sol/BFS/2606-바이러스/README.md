# 📝 Baekjoon 2606: 바이러스

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![실버 3](https://img.shields.io/badge/Silver-3-949393?style=for-the-badge) | `BFS` | [2606번 문제](https://www.acmicpc.net/problem/2606) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 그래프의 너비 우선 탐색(BFS)을 이용하여 연결 요소의 크기를 구하는 문제를 해결합니다.  입력으로 주어지는 그래프는 무방향 그래프이며, 1번 노드부터 시작하여 BFS를 수행하여 방문한 노드의 개수를 세어 연결 요소의 크기를 계산합니다.  결과에서 1을 뺀 값을 출력하는 이유는 시작 노드인 1번 노드를 제외한 연결된 노드의 개수를 구하기 위함입니다.


### 📝 **알고리즘**

1. **입력:** 노드의 개수 `n`과 간선의 개수 `com`을 입력받습니다.  각 노드에 연결된 노드들을 저장할 인접 리스트 `node`를 생성하고, 방문 여부를 저장할 `visited` 배열을 초기화합니다.
2. **그래프 생성:** `com` 개의 간선 정보를 입력받아 무방향 그래프 `node`를 구성합니다.  `node[a].append(b)` 와 `node[b].append(a)` 를 통해 a와 b 노드 간의 양방향 연결을 표현합니다.
3. **BFS 수행:** `virus()` 함수에서 deque를 이용하여 BFS를 수행합니다. 1번 노드부터 시작하여 방문하지 않은 노드를 방문하고, 방문한 노드를 `result` 리스트에 추가합니다. 방문한 노드는 `visited` 배열을 통해 관리합니다.  각 노드의 인접 노드들을 큐에 추가하여 탐색을 진행합니다.
4. **결과 출력:** `virus()` 함수가 반환하는 `result` 리스트의 길이에서 1을 뺀 값을 출력합니다. 이는 시작 노드 1을 제외한 연결된 노드의 개수를 의미합니다.


### 🧐 **시간 복잡도**

BFS 알고리즘을 사용하므로, 시간 복잡도는 O(V + E) 입니다. 여기서 V는 노드의 개수, E는 간선의 개수입니다.  각 노드는 최대 한 번 방문하고, 각 간선은 최대 두 번(양방향) 탐색되기 때문입니다.  따라서 입력 크기가 커지더라도 효율적으로 문제를 해결할 수 있습니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 2606: 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque

def virus():
    result = []
    stack = deque([1])
    while stack:
        now = stack.popleft()
        if not visited[now]:
            result.append(now)
            visited[now] = True
            for data in node[now]:
                stack.append(data)
    return result
n = int(input())

com = int(input())

node = {}
for i in range(n):
    node[i+1] = []

for _ in range(com):
    a,b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visited = [False] * (n+1)

print(len(virus())-1)
</details>