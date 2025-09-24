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

