import sys

input = sys.stdin.readline

from collections import deque

T = int(input())
list_num = deque()
for i in range(T):
    order = input()
    if len(order) > 2:
        order_list = list(map(int,order.split()))
        if order_list[0] == 1:
            list_num.appendleft(order_list[1])
        else:
            list_num.append(order_list[1])
    
    else:
        order = int(order)
        if order == 3:
            if not list_num:
                print(-1)
            else:
                print(list_num.popleft())
        if order == 4:
            if not list_num:
                print(-1)
            else:
                print(list_num.pop())
        if order == 5:
            print(len(list_num))
        if order == 6:
            if not list_num:
                print(1)
            else:
                print(0)
        
        if order == 7:
            if list_num:
                print(list_num[0])
            else:
                print(-1)

        if order == 8:
            if not list_num:
                print(-1)
            else:
                print(list_num[-1])
                        
