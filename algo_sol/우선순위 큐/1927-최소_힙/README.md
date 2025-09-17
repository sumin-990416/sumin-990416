# 📝 Baekjoon 1927: 최소 힙

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-17 | ![실버 2](https://img.shields.io/badge/Silver-2-949393?style=for-the-badge) | `우선순위 큐` | [1927번 문제](https://www.acmicpc.net/problem/1927) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

힙(Heap) 자료구조를 이용하여 최소 힙을 구현하여, 입력받는 정수를 관리한다.  0이 입력되면 최소 힙에서 가장 작은 값(최소값)을 출력하고, 0이 아닌 정수는 최소 힙에 추가한다.  힙 자료구조의 특성을 이용하여 최소값을 O(1) 시간에 접근하고 삭제하는 것이 핵심이다.  힙이 비어있을 경우 0을 출력한다.

### 📝 **알고리즘**

1. **입력:** 테스트 케이스의 개수 `T`를 입력받는다.
2. **힙 초기화:** 최소 힙을 구현하기 위해 `heapq` 모듈을 사용한다. 빈 리스트 `arr`을 최소 힙으로 사용한다.
3. **반복:** `T`번 반복하며, 매 반복마다 정수 `n`을 입력받는다.
4. **조건 분기:**
   - `n`이 0이 아닌 경우: `n`을 최소 힙 `arr`에 추가한다 (`heapq.heappush`).
   - `n`이 0인 경우:
     - `arr`이 비어있으면 (즉, 힙에 원소가 없으면) 0을 출력한다.
     - `arr`이 비어있지 않으면, `arr`에서 최소값을 제거하고 출력한다 (`heapq.heappop`).
5. **반복 종료:** 모든 테스트 케이스를 처리하면 종료한다.

### 🧐 **시간 복잡도**

- `heapq.heappush` 연산은 O(log N)의 시간 복잡도를 가진다.  N은 힙의 크기이다.
- `heapq.heappop` 연산 또한 O(log N)의 시간 복잡도를 가진다.
- 입력되는 정수의 개수가 T개이고, 각 정수에 대한 연산이 최대 O(log T) 시간이 걸리므로, 전체 알고리즘의 시간 복잡도는 O(T log T)이다.  힙의 크기가 최대 T이기 때문이다.  최악의 경우 모든 입력이 0이 아닌 정수일 때 T개의 원소를 힙에 저장하고, 마지막에 T개의 0이 입력되어 T개의 `heapq.heappop` 연산을 수행할 수 있다.




<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1927: 최소 힙
# https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    if n != 0:
        heapq.heappush(arr,n)
    else:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
</details>