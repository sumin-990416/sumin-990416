def find_rank(num1,num2):
    rank = 1
    for i in range(n):
        if num1 < list_num[i][0] and num2 < list_num[i][1]:
            rank += 1
    return rank



n = int(input())

list_num = []
for _ in range(n):
    kg,cm = map(int,input().split())
    list_num.append([kg,cm])

result = []
for i in range(n):
    kg_i, cm_i = list_num[i]
    result.append(find_rank(kg_i,cm_i))

print(*result)