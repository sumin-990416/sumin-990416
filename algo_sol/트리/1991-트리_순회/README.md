# 📝 Baekjoon 1991: 트리 순회

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-12 | ![실버 1](https://img.shields.io/badge/Silver-1-949393?style=for-the-badge) | `트리` | [1991번 문제](https://www.acmicpc.net/problem/1991) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

입력으로 주어지는 트리 정보를 이용하여 이진 트리를 생성하고, 전위 순회, 중위 순회, 후위 순회를 수행하는 알고리즘이다.  핵심은 입력 데이터를 효율적으로 처리하여 트리의 구조를 메모리에 재구성하는 것이다.  딕셔너리를 활용하여 노드들을 저장하고,  각 노드에 대한 왼쪽 및 오른쪽 자식 노드를 연결함으로써 트리 구조를 효과적으로 표현한다.


### 📝 **알고리즘**

1. **입력:**  N개의 노드 정보를 입력받는다. 각 노드 정보는 (노드 데이터, 왼쪽 자식 노드 데이터, 오른쪽 자식 노드 데이터) 형태로 주어진다.  `.`은 자식 노드가 없음을 의미한다.

2. **트리 생성:**  `Node` 클래스를 이용하여 노드들을 생성하고, 딕셔너리 `nodes`에 노드 데이터를 키로, 노드 객체를 값으로 저장한다. 입력 데이터를 순회하며, 각 노드에 대해 왼쪽 및 오른쪽 자식 노드를 연결한다.  자식 노드가 딕셔너리에 없다면 새로운 노드를 생성하여 추가하고 연결한다.

3. **트리 순회:** 루트 노드 ('A')를 찾아 전위 순회(`preorder_traversal`), 중위 순회(`inorder_traversal`), 후위 순회(`postorder_traversal`) 함수를 호출하여 각 순회 결과를 출력한다.  각 순회 함수는 재귀적으로 트리를 탐색하며 노드의 데이터를 출력한다.

### 🧐 **시간 복잡도**

- 트리 생성: 입력 노드의 수 N에 비례하는 시간이 걸린다. 각 노드에 대해 왼쪽 및 오른쪽 자식 노드를 연결하는 연산이 상수 시간에 이루어지므로 O(N)의 시간 복잡도를 가진다.
- 트리 순회: 각 순회 함수는 트리의 모든 노드를 한 번씩 방문하므로, 노드의 수 N에 비례하는 시간이 걸린다. 따라서 O(N)의 시간 복잡도를 가진다.

따라서 전체 알고리즘의 시간 복잡도는 O(N)이다.  공간 복잡도는 트리의 노드 수 N에 비례하므로 O(N)이다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1991: 트리 순회
# https://www.acmicpc.net/problem/1991

import sys


# 재귀 깊이 제한을 풀어주는 것이 좋습니다 (트리가 깊을 경우 대비)
# sys.setrecursionlimit(10**6)

# 1. 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 순회 함수들은 이전과 동일합니다.
def preorder_traversal(node):
    if node:
        print(node.data, end='')
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end='')
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end='')


# 2. 동적으로 트리 생성하기
if __name__ == "__main__":
    n = int(sys.stdin.readline())

    # 노드들을 저장할 딕셔너리
    nodes = {}

    for _ in range(n):
        data, left_data, right_data = sys.stdin.readline().strip().split()

        # --- 핵심 로직 ---
        # 부모 노드가 딕셔너리에 없으면 생성하여 추가
        if data not in nodes:
            nodes[data] = Node(data)

        # 왼쪽 자식 노드 처리
        if left_data != '.':
            # 자식 노드가 딕셔너리에 없으면 생성하여 추가
            if left_data not in nodes:
                nodes[left_data] = Node(left_data)
            # 부모와 자식 연결
            nodes[data].left = nodes[left_data]

        # 오른쪽 자식 노드 처리
        if right_data != '.':
            # 자식 노드가 딕셔너리에 없으면 생성하여 추가
            if right_data not in nodes:
                nodes[right_data] = Node(right_data)
            # 부모와 자식 연결
            nodes[data].right = nodes[right_data]

    # 3. 순회 시작
    # 보통 문제에서는 'A'가 루트 노드라고 알려줍니다.
    root_node = nodes['A']

    preorder_traversal(root_node)
    print()
    inorder_traversal(root_node)
    print()
    postorder_traversal(root_node)
    print()
</details>