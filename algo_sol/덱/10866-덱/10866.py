from collections import deque
import sys

n = int(sys.stdin.readline())
list_num = deque()

for _ in range(n):
    order = sys.stdin.readline()
    if 'push_back' in order:
        order_m, num = order.split()
        list_num.append(num)

    elif  'pop_back' in order:
        if not list_num:
            print(-1)
        else:
            print(list_num.pop())

    elif 'back' in order:
        if not list_num:
            print(-1)
        else:
            print(list_num[-1])

    if 'push_front' in order:
        order_m, num = order.split()
        list_num.appendleft(num)
    
    elif 'pop_front' in order:
        if not list_num:
            print(-1)
        else:
            print(list_num.popleft())

    elif 'front' in order:
        if not list_num:
            print(-1)
        else:
            print(list_num[0])
    
    
    if 'size' in order:
        print(len(list_num))
    
    if 'empty' in order:
        if not list_num:
            print(1)
        else:
            print(0)