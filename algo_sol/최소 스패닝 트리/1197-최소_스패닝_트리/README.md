# 📝 Baekjoon 1197: 최소 스패닝 트리

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-17 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `최소 스패닝 트리` | [1197번 문제](https://www.acmicpc.net/problem/1197) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

크루스칼 알고리즘을 이용하여 최소 신장 트리를 구현합니다.  간선들을 비용 순으로 정렬하고, 사이클이 발생하지 않는 간선들만 선택하여 최소 비용의 신장 트리를 만듭니다.  Union-Find 알고리즘을 사용하여 사이클 검출 및 집합 연산을 효율적으로 수행합니다.

### 📝 **알고리즘**

1. **입력:** 정점의 개수 `v`, 간선의 개수 `e`, 각 간선의 비용과 연결된 두 정점 정보를 입력받습니다.
2. **초기화:** 각 정점을 부모 노드로 가지는 Union-Find 자료구조 `parent`를 초기화합니다.
3. **간선 정렬:** 입력받은 간선들을 비용을 기준으로 오름차순으로 정렬합니다.
4. **크루스칼 알고리즘:** 정렬된 간선들을 순회하며, 각 간선에 대해 Union-Find를 이용하여 사이클을 검사합니다.
    - 만약 사이클이 발생하지 않는다면 (두 정점이 다른 집합에 속한다면), 해당 간선을 최소 신장 트리에 포함시키고, `union_parent` 함수를 이용하여 두 정점을 합쳐줍니다.  그리고 간선의 비용을 `result`에 더합니다.
5. **출력:** 최소 신장 트리의 총 비용 `result`를 출력합니다.

### 🧐 **시간 복잡도**

- 간선 정렬: O(E log E)  (E는 간선의 개수)
- Union-Find 연산 (find_parent, union_parent):  경로 압축과 합침 과정을 통해,  평균적으로 O(α(V)) (α는 아커만 함수의 역함수로 매우 느리게 증가하는 함수, V는 정점의 개수)의 시간 복잡도를 가집니다.  실제로는 거의 상수 시간에 가깝게 동작합니다.
- 전체적인 시간 복잡도는 간선 정렬의 시간 복잡도가 지배적이므로, O(E log E) 입니다.  V가 E보다 작거나 비슷한 크기인 경우, O(E log E)는 O(V log V) 와 비슷한 시간 복잡도를 가집니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1197: 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197

import sys

# 재귀 깊이 제한 해제 (백준 채점 시 필요할 수 있음)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  # 빠른 입력을 위해 추가


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 정점의 개수와 간선의 개수
v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(1, v + 1):  # 1부터 v까지 초기화
    parent[i] = i

edges = []
result = 0

# 1. 입력받는 즉시 (비용, 정점1, 정점2) 형태로 저장
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 정렬을 위해 cost를 맨 앞에 둔다

# 2. 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    # 3. 올바른 순서로 변수 할당
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
</details>