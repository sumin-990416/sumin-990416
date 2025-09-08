# 📝 Baekjoon 10866: 덱

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-08 | ![실버 4](https://img.shields.io/badge/Silver-4-949393?style=for-the-badge) | `덱` | [10866번 문제](https://www.acmicpc.net/problem/10866) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

데크(deque) 자료구조를 활용하여  `push_front`, `push_back`, `pop_front`, `pop_back`, `front`, `back`, `size`, `empty` 연산을 처리하는 문제입니다.  입력으로 주어지는 명령어에 따라 데크에 원소를 추가하거나 제거하고, 또는 데크의 상태(크기, 비어있는지 여부, 앞/뒤 원소)를 출력합니다.  데크의 특징인 양쪽 끝에서의 효율적인 삽입 및 삭제 연산을 이용하여 문제를 해결합니다.


### 📝 **알고리즘**

1. **입력:** 표준 입력으로부터 명령어의 개수 `n`과 `n`개의 명령어를 입력받습니다.
2. **데크 초기화:** `collections.deque`를 이용하여 빈 데크 `list_num`을 생성합니다.
3. **명령어 처리:** 입력받은 각 명령어를 순차적으로 처리합니다.  각 명령어는 다음과 같이 처리됩니다.
    - `push_front X`:  `X`를 데크의 앞쪽에 추가합니다.
    - `push_back X`: `X`를 데크의 뒤쪽에 추가합니다.
    - `pop_front`: 데크의 앞쪽에서 원소를 제거하고 출력합니다. 데크가 비어있으면 -1을 출력합니다.
    - `pop_back`: 데크의 뒤쪽에서 원소를 제거하고 출력합니다. 데크가 비어있으면 -1을 출력합니다.
    - `front`: 데크의 앞쪽 원소를 출력합니다. 데크가 비어있으면 -1을 출력합니다.
    - `back`: 데크의 뒤쪽 원소를 출력합니다. 데크가 비어있으면 -1을 출력합니다.
    - `size`: 데크의 크기를 출력합니다.
    - `empty`: 데크가 비어있으면 1, 아니면 0을 출력합니다.
4. **출력:** 각 명령어 처리 결과를 표준 출력으로 출력합니다.


### 🧐 **시간 복잡도**

각 명령어 처리에 걸리는 시간은 대부분 O(1)입니다.  `deque` 자료구조의 `append`, `appendleft`, `pop`, `popleft` 연산은 상수 시간에 수행되기 때문입니다.  `size`와 `empty` 연산 역시 상수 시간에 수행됩니다.  따라서 전체 알고리즘의 시간 복잡도는 입력으로 주어지는 명령어의 개수 `n`에 비례하는 O(n)입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 10866: 덱
# https://www.acmicpc.net/problem/10866

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
</details>