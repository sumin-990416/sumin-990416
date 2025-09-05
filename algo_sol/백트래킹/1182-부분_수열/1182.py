n, m = map(int,input().split())

list_num = list(map(int,input().split()))


count_num = 0
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(list_num[j])
    if sum(subset) == m and subset:
        count_num += 1

print(count_num)