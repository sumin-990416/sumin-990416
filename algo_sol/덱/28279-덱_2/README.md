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

    ### ❌ AI 분석 실패
- 오류: 404 models/gemini-pro is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.
- API 키가 정확한지, 환경 변수 설정이 올바르게 되었는지 확인해주세요.

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