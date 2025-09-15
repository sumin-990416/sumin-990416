n, m = map(int,input().split())

result = ''
result_n = 0
list_dna = []
for _ in range(n):
    list_dna.append(input())


for j in range(m):
    list_num = [0,0,0,0]
    for i in range(n):
        if list_dna[i][j] == 'A':
            list_num[0] += 1
        if list_dna[i][j] == 'C':
            list_num[1] += 1
        if list_dna[i][j] == 'G':
            list_num[2] += 1
        if list_dna[i][j] == 'T':
            list_num[3] += 1
    
    idx = 0
    for i in range(4):
        if list_num[i] > list_num[idx]:
            idx = i
    result_n += n - list_num[idx]
    if idx == 0:
        result += 'A'
    if idx == 1:
        result += 'C'
    if idx == 2:
        result += 'G'
    if idx == 3:
        result += 'T'

print(result)
print(result_n)
    