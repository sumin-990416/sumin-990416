from itertools import combinations
n_list = []
while True:
    num_list = list(map(int,input().split()))
    n = num_list[0]
    if n == 0:
        break
    num = num_list[1:]
    num.sort()
    n_list.append(num)

for i in range(len(n_list)):
    comb = list(combinations(n_list[i],6))
    for com in comb:
        print(*com)
    print()