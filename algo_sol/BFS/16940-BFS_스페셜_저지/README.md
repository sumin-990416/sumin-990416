# 📝 Baekjoon 16940: BFS 스페셜 저지

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![골드 3](https://img.shields.io/badge/Gold-3-E5A323?style=for-the-badge) | `BFS` | [16940번 문제](https://www.acmicpc.net/problem/16940) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 주어진 트리에서 노드들의 순서가 주어졌을 때, 그 순서대로 노드들을 방문할 수 있는지 확인하는 문제를 해결합니다.  BFS(Breadth-First Search)를 변형하여, 주어진 순서대로 노드를 방문하기 위해 방문 가능한 노드들을 `stack`에 저장하고,  현재 방문해야 할 노드가 `stack`에 존재하는지 확인하며 순차적으로 방문 가능 여부를 판단합니다.  만약 주어진 순서대로 방문이 불가능하면 0을, 가능하면 1을 반환합니다.


### 📝 **알고리즘**

1. **입력:** 노드의 개수 `n`과 트리의 간선 정보, 그리고 노드 방문 순서 `arr`을 입력받습니다.  `node` 리스트는 각 노드에 연결된 노드들을 저장하는 인접 리스트를 나타냅니다.

2. **BFS 변형:**  `stack`이라는 deque를 이용하여 BFS와 유사한 방식으로 노드를 방문합니다. `stack`의 가장 앞에 있는 노드부터 순차적으로 방문 대상을 검토합니다.

3. **순서 확인:** `arr`의 각 노드에 대해, 현재 `stack`에 방문 가능한 노드가 있는지 확인합니다.  현재 방문해야 할 노드(`i`)가 `stack`의 현재 노드(`stack[idx]`)의 인접 노드(`node[stack[idx]]`)에 존재하지 않으면 `idx`를 증가시켜 `stack`의 다음 노드를 검토합니다.

4. **방문 불가능 판단:** `idx`가 `stack`의 크기를 넘어서는 경우, 주어진 순서대로 방문이 불가능하다는 것을 의미하므로 0을 반환합니다.

5. **방문 가능 판단:** `arr`의 모든 노드를 순서대로 방문할 수 있는 경우, 1을 반환합니다.


### 🧐 **시간 복잡도**

- 트리의 간선 정보 입력: O(n)
- 노드 방문 순서 입력: O(n)
- BFS 변형 과정: 최악의 경우 모든 노드를 여러 번 검사할 수 있으므로 O(n²)에 가까운 시간 복잡도를 가집니다.  하지만 실제로는 트리 구조의 특성상 모든 노드를 반복적으로 검사하는 경우는 드물며, 평균적으로 O(n)에 가까운 성능을 보일 것으로 예상됩니다.  따라서 시간 복잡도는 O(n²)으로 분석할 수 있으나, 실제 수행 시간은 O(n)에 가까울 수 있습니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 16940: BFS 스페셜 저지
# https://www.acmicpc.net/problem/16940

from collections import deque

def bfs():
    stack = deque([0])
    idx = 0
    for i in arr:
        while i not in node[stack[idx]]:
            idx += 1
            if idx == len(stack):
                return 0
        stack.append(i)
    return 1

n = int(input())

node = [set() for _ in range(n+1)]

node[0].add(1)

for i in range(n-1):
    parents , child = map(int,input().split())
    node[parents].add(child)
    node[child].add(parents)

arr = list(map(int,input().split()))

print(bfs())
</details>