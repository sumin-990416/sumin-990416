# 📝 Baekjoon 28279: 덱 2

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-03 | ![실버 4](https://img.shields.io/badge/Silver-4-949393?style=for-the-badge) | `덱` | [28279번 문제](https://www.acmicpc.net/problem/28279) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 데크(deque) 자료구조를 이용하여 큐와 스택의 기능을 동시에 구현하는 문제를 해결합니다.  입력으로 들어오는 명령어에 따라 데크의 앞 또는 뒤에 원소를 추가하거나, 앞 또는 뒤에서 원소를 제거하고, 데크의 크기 또는 비어있는지 여부를 확인하는 등의 연산을 수행합니다.  핵심은 데크의 `appendleft()`, `append()`, `popleft()`, `pop()` 메서드를 효율적으로 활용하여 문제에서 요구하는 기능을 구현하는 것입니다.


### 📝 **알고리즘**

코드는 `T`번의 명령어를 처리합니다. 각 명령어는 정수 하나 또는 정수 두 개로 구성됩니다.

1. **명령어 입력 및 처리:**  입력받은 명령어의 길이를 확인하여 명령어의 종류를 구분합니다.  길이가 2보다 큰 경우(1 또는 2번 명령어), 정수 두 개를 입력받아  `order_list[0]`가 1이면 데크의 앞(`appendleft()`)에, 2이면 데크의 뒤(`append()`)에 `order_list[1]`을 추가합니다.  길이가 2 이하인 경우(3~8번 명령어), 정수 하나를 입력받아 명령어에 따라 다음과 같은 연산을 수행합니다.

2. **명령어별 연산:**
    - 3번 명령어: 데크의 앞에서 원소를 제거하고 출력(`popleft()`). 데크가 비어있으면 -1 출력.
    - 4번 명령어: 데크의 뒤에서 원소를 제거하고 출력(`pop()`). 데크가 비어있으면 -1 출력.
    - 5번 명령어: 데크의 크기를 출력.
    - 6번 명령어: 데크가 비어있으면 1, 아니면 0 출력.
    - 7번 명령어: 데크의 첫 번째 원소를 출력. 데크가 비어있으면 -1 출력.
    - 8번 명령어: 데크의 마지막 원소를 출력. 데크가 비어있으면 -1 출력.


### 🧐 **시간 복잡도**

각 명령어 처리에 필요한 시간은 상수 시간(O(1))입니다. 데크의 `appendleft()`, `append()`, `popleft()`, `pop()` 연산은 모두 상수 시간에 수행되기 때문입니다.  `T`개의 명령어를 처리하므로 전체 시간 복잡도는 O(T)입니다.  입력 크기 T에 선형적으로 비례하는 시간이 걸립니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
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
</details>