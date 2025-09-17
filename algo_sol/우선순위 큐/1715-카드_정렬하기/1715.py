import heapq
import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    heapq.heappush(arr,int(input()))
result = 0
while len(arr) > 1:
    now = heapq.heappop(arr)
    now2 = heapq.heappop(arr)
    result += now+now2
    arr.append(now+now2)

print(result)