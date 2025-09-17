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