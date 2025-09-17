# 📝 Baekjoon 11279: 최대 힙

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-17 | ![실버 2](https://img.shields.io/badge/Silver-2-949393?style=for-the-badge) | `우선순위 큐` | [11279번 문제](https://www.acmicpc.net/problem/11279) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

힙(Heap) 자료구조를 이용하여 최댓값을 효율적으로 관리하는 것이다.  입력값이 0이 아닌 경우, 음수로 변환하여 최대힙에 삽입하고, 0인 경우 최대힙에서 최댓값을 추출하여 출력한다.  음수로 변환하는 이유는 Python의 `heapq` 모듈이 최소힙을 기본으로 제공하기 때문이며, 최소힙에 음수를 넣으면 최댓값을 쉽게 관리할 수 있다.

### 📝 **알고리즘**

1. **입력:**  T개의 정수를 입력받는다.
2. **힙 관리:** 입력받은 정수가 0이 아니면 음수로 변환하여 최대힙 `arr`에 삽입한다 (`heapq.heappush`).  0이면 최대힙 `arr`이 비어있는지 확인한다.
3. **출력:** 최대힙이 비어있으면 0을 출력하고, 비어있지 않으면 최대힙에서 최댓값(음수로 저장되어 있으므로, -를 붙여 양수로 변환)을 추출하여 출력한다 (`heapq.heappop`).

### 🧐 **시간 복잡도**

힙에 원소를 삽입하거나 추출하는 연산은 모두 O(logN)의 시간 복잡도를 갖는다.  N은 힙에 저장된 원소의 최대 개수이다.  따라서 전체 알고리즘의 시간 복잡도는 O(T logN)이 된다.  T는 입력으로 주어진 정수의 개수이고, N은 최대 힙에 들어있는 원소의 개수이며 T와 N은 최악의 경우 같을 수 있다.  입력 횟수 T에 비례하는 시간 복잡도를 갖는다고 볼 수 있다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 11279: 최대 힙
# https://www.acmicpc.net/problem/11279

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
</details>