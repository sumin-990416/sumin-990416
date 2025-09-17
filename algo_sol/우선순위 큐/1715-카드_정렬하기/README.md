# 📝 Baekjoon 1715: 카드 정렬하기

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-17 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `우선순위 큐` | [1715번 문제](https://www.acmicpc.net/problem/1715) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

힙(Heap) 자료구조를 이용하여 최소 힙을 구현하고,  최소 두 개의 원소를 반복적으로 합쳐서 최소 비용을 구하는 허프만 코딩(Huffman Coding) 알고리즘의 아이디어를 응용한 문제 해결 방식입니다.  가장 작은 두 개의 수를 반복적으로 더하여 최소값의 합을 구함으로써 문제에서 요구하는 최소 비용을 효율적으로 계산합니다.


### 📝 **알고리즘**

1. **입력:** T개의 정수를 입력받아 최소 힙(min-heap) `arr`에 저장합니다.  `heapq` 모듈을 사용하여 최소 힙을 효율적으로 관리합니다.
2. **반복:** 힙에 원소가 하나 남을 때까지 다음을 반복합니다.
   - 힙에서 가장 작은 두 원소 `now`와 `now2`를 `heapq.heappop()`으로 추출합니다.
   - 두 원소의 합 `now + now2`를 `result`에 더합니다. (최소 비용 누적)
   - 두 원소의 합을 다시 힙 `arr`에 `heapq.heappush()`로 추가합니다.
3. **출력:** 최종적으로 계산된 `result` (최소 비용의 합)을 출력합니다.


### 🧐 **시간 복잡도**

힙에 T개의 원소를 삽입하는 데는 O(T log T)의 시간이 걸립니다.  `while` 루프는 최대 T-1번 반복되며, 각 반복마다 힙에서 두 원소를 추출하고 하나의 원소를 삽입하는 연산이 수행됩니다. 힙에서 원소를 추출하고 삽입하는 연산은 모두 O(log T)의 시간 복잡도를 가지므로, 전체 `while` 루프의 시간 복잡도는 O(T log T)입니다. 따라서 전체 알고리즘의 시간 복잡도는 O(T log T)입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1715: 카드 정렬하기
# https://www.acmicpc.net/problem/1715

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
</details>