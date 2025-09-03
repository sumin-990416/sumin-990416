#  Baekjoon 28279: 덱 2

    - **Solved Date**: 2025-09-03
    - **Problem Link**: [https://www.acmicpc.net/problem/28279](https://www.acmicpc.net/problem/28279)
    - **Difficulty**: 실버 4
    - **Algorithm**: 덱

    ---

    ## ✅ Solution Status

    **Solved!** ✔️

    ---

    ## 🤖 AI Code Analysis

    ### 🧠 **핵심 아이디어**

이 코드는 덱(deque) 자료구조를 이용하여 양쪽 끝에서 원소를 삽입 및 삭제하는 연산을 효율적으로 처리하는 문제를 해결합니다.  입력으로 주어지는 명령어에 따라 덱에 원소를 왼쪽 또는 오른쪽에 추가하거나, 왼쪽 또는 오른쪽에서 원소를 제거하고, 덱의 크기 또는 비어있는지 여부를 확인하는 등의 작업을 수행합니다.  핵심은 덱의 `appendleft()`, `append()`, `popleft()`, `pop()` 메서드를 활용하여 문제에서 요구하는 연산들을 효율적으로 구현하는 것입니다.


### 📝 **알고리즘**

1. **입력:** T개의 명령어를 입력받습니다. 각 명령어는 정수 하나 또는 정수 두 개로 구성됩니다.

2. **명령어 처리:**  각 명령어를 처리합니다.
    * 명령어가 1 또는 2인 경우: 덱에 원소를 추가합니다. 1이면 왼쪽에, 2이면 오른쪽에 추가합니다.
    * 명령어가 3인 경우: 덱의 왼쪽에서 원소를 제거하고 출력합니다. 덱이 비어있으면 -1을 출력합니다.
    * 명령어가 4인 경우: 덱의 오른쪽에서 원소를 제거하고 출력합니다. 덱이 비어있으면 -1을 출력합니다.
    * 명령어가 5인 경우: 덱의 크기를 출력합니다.
    * 명령어가 6인 경우: 덱이 비어있으면 1을, 아니면 0을 출력합니다.
    * 명령어가 7인 경우: 덱의 맨 앞 원소를 출력합니다. 덱이 비어있으면 -1을 출력합니다.
    * 명령어가 8인 경우: 덱의 맨 뒤 원소를 출력합니다. 덱이 비어있으면 -1을 출력합니다.

3. **출력:** 각 명령어에 대한 결과를 출력합니다.


### 🧐 **시간 복잡도**

각 명령어 처리에 필요한 시간은 O(1)입니다.  덱의 `appendleft()`, `append()`, `popleft()`, `pop()` 연산은 모두 상수 시간에 수행되기 때문입니다. 따라서 전체 알고리즘의 시간 복잡도는 입력받는 명령어의 개수 T에 비례하는 O(T)가 됩니다.


    ---

    ## 💻 My Code

    ```py
    # Baekjoon Problem 28279: 덱 2
    # https://www.acmicpc.net/problem/28279

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