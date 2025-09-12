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