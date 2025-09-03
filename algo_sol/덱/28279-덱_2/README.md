#  Baekjoon 28279: 덱 2

- **Solved Date**: 2025-09-03
- **Problem Link**: [https://www.acmicpc.net/problem/28279](https://www.acmicpc.net/problem/28279)
- **Difficulty**: 실버 4
- **Algorithm**: 덱

---

## ✅ Solution Status

**Solved!** ✔️

---

## 🤖 AI Summary

### 🧠 **핵심 아이디어**
- 문제의 핵심 요구사항을 어떤 방식으로 접근하여 해결했는지에 대한 요약입니다.
- (예: '최단 거리를 구해야 하므로 BFS를 활용했습니다.')

### 📝 **알고리즘**
- **자료구조**: 사용한 주요 자료구조 (예: `deque`를 이용한 큐, 우선순위 큐 등)
- **알고리즘**: 적용한 핵심 알고리즘 (예: 너비 우선 탐색 (BFS), 동적 계획법 (DP))

### 🧐 **시간 복잡도**
- 이 풀이의 시간 복잡도는 $O(V+E)$ 입니다. (V: 정점의 수, E: 간선의 수)
- (예시이며, 실제 분석 결과는 코드에 따라 달라집니다.)

### 🤔 **어려웠던 점**
- 구현 중 겪었던 문제나, 특정 테스트 케이스를 통과하기 위해 고민했던 부분을 기록합니다.
- (예: '시간 초과를 해결하기 위해 `sys.stdin.readline`을 사용했습니다.')

---

## 💻 My Code

```python
# Baekjoon Problem 28279: 덱 2
# [https://www.acmicpc.net/problem/](https://www.acmicpc.net/problem/)28279

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
