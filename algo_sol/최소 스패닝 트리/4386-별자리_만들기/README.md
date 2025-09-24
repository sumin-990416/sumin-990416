# 📝 Baekjoon 4386: 별자리 만들기

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-24 | ![골드 3](https://img.shields.io/badge/Gold-3-E5A323?style=for-the-badge) | `최소 스패닝 트리` | [4386번 문제](https://www.acmicpc.net/problem/4386) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 크루스칼 알고리즘을 이용하여 n개의 점들 사이의 최소 신장 트리(MST, Minimum Spanning Tree)를 구현합니다.  n개의 점들의 좌표가 주어지면, 각 점들을 노드로, 점들 사이의 거리를 가중치로 하는 그래프를 구성합니다. 크루스칼 알고리즘은 가중치가 가장 작은 간선부터 선택하며, 사이클이 발생하지 않도록 간선을 추가하여 MST를 생성합니다.  합집합 자료구조(Union-Find)를 사용하여 사이클 검출을 효율적으로 수행합니다.

### 📝 **알고리즘**

1. **입력:** n개의 점들의 (x, y) 좌표를 입력받습니다.
2. **간선 생성:** 모든 점 쌍 사이의 거리를 계산하여 간선 목록 `mst_list`를 생성합니다. 각 간선은 (거리, 점1의 인덱스, 점2의 인덱스)의 튜플로 표현됩니다.
3. **정렬:** 간선 목록 `mst_list`를 거리(가중치)를 기준으로 오름차순으로 정렬합니다.
4. **크루스칼 알고리즘:**
    - `parent` 배열을 사용하여 Union-Find 자료구조를 초기화합니다. 각 점은 처음에는 자기 자신을 부모 노드로 갖습니다.
    - 정렬된 간선 목록을 순회하며, 각 간선에 대해 다음을 수행합니다.
        - `find_parent` 함수를 사용하여 간선의 두 점이 이미 같은 집합에 속하는지 확인합니다.
        - 같은 집합에 속하지 않으면 (사이클이 발생하지 않으면), `union_parent` 함수를 사용하여 두 점을 같은 집합으로 합치고, 간선의 가중치를 `result`에 더합니다.
5. **출력:** 최소 신장 트리의 총 가중치 `result`를 소수점 둘째 자리까지 출력합니다.


### 🧐 **시간 복잡도**

- 간선 생성:  O(n²) - 모든 점 쌍에 대해 거리를 계산해야 하므로.
- 정렬: O(E log E) - E는 간선의 개수 (최대 O(n²)) 이므로 O(n² log n²)
- 크루스칼 알고리즘: O(E log V) - E는 간선의 개수, V는 정점의 개수 (n) 이므로 O(n² log n) (Union-Find 연산의 시간복잡도는 경로압축과 병합을 고려하면 거의 상수시간에 가깝습니다)

따라서 전체 알고리즘의 시간 복잡도는 O(n² log n) 입니다.  정렬 과정이 지배적입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 4386: 별자리 만들기
# https://www.acmicpc.net/problem/4386

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,x,y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

arr = []

for _ in range(n):
    x,y = map(float,input().split())
    arr.append((x,y))

parent = [0]*n
for i in range(n):
    parent[i] = i

mst_list = []
for i in range(n):
    for j in range(i+1,n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]
        mst_list.append((((x1-x2)**2 + (y1-y2)**2)**(1/2),i,j))

result = 0.0
mst_list.sort()
for edge in mst_list:
    cost, x, y = edge
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        result += cost

print(f'{result:.2f}')
</details>