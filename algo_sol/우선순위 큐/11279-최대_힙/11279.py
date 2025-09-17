import heapq
import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    if n != 0:
        heapq.heappush(arr,-n)
    else:
        if not arr:
            print(0)
        else:
            print(-heapq.heappop(arr))