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