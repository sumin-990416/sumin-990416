from itertools import permutations

n = int(input())

num_list = [i+1 for i in range(n)]

for i in permutations(num_list,n):
    print(*i)