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