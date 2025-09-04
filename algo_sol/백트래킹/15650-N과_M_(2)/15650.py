def make_num(m, start):
    if m == M:
        last.append(result.copy())
        return
    
    
    for i in range(N):
        if not result:
            result.append(i+1)
            make_num(m+1, i+1)
            result.pop()
        else:
            if result[-1] < i+1:
                result.append(i+1)
                make_num(m+1, i+1)
                result.pop()




N, M = map(int,input().split())

last = []
result = []


visited = [False] * N
make_num(0,0)

final = []
for i in range(len(last)):
    if last[i] not in final:
        final.append(last[i])

for i in range(len(final)):
    print(*final[i])