N, M = map(int,input().split())

result = []
def make_num(m):
    if m == M:
        print(*result)
        return
    for i in range(N):
        if (i + 1) in result:
            continue
        else:
            result.append(i+1)
            make_num(m+1)
            result.pop()


make_num(0)