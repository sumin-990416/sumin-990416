import heapq

def dijkstra():
    money_sum = [[float('inf')]*n for _ in range(n)]

    prior =[]

    heapq.heappush(prior, (arr[0][0],0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while prior:
        money, x, y = heapq.heappop(prior)

        if money > money_sum[x][y]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n:
                new_money = money + arr[nx][ny]

                if new_money < money_sum[nx][ny]:
                    money_sum[nx][ny] = new_money
                    heapq.heappush(prior,(new_money,nx,ny))
    return money_sum[-1][-1]



i = 1
while True:
    n = int(input())
    if n == 0:
        break

    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    print(f'Problem {i}: {dijkstra()}')
    i += 1