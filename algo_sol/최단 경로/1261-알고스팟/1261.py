import heapq

def dijkstra():
    money_sum = [[float('inf')]*n for _ in range(m)]
    money_sum[0][0] = 0
    prior =[]

    heapq.heappush(prior, (arr[0][0],0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while prior:
        money, x, y = heapq.heappop(prior)

        if money > money_sum[y][x]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m:
                new_money = money + arr[ny][nx]

                if new_money < money_sum[ny][nx]:
                    money_sum[ny][nx] = new_money
                    heapq.heappush(prior,(new_money,nx,ny))
    return money_sum[-1][-1]



n, m = map(int,input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int,input())))
print(dijkstra())