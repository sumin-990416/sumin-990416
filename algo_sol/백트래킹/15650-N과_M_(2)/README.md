# 📝 Baekjoon 15650: N과 M (2)

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-04 | ![실버 3](https://img.shields.io/badge/Silver-3-949393?style=for-the-badge) | `백트래킹` | [15650번 문제](https://www.acmicpc.net/problem/15650) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

본 코드는 중복되지 않는 수열을 생성하는 재귀 함수 `make_num`을 사용하여 N개의 자연수 중에서 M개를 순서있게 선택하는 조합을 구현합니다.  `result` 리스트에 선택된 수들을 저장하고, 재귀 호출을 통해 모든 조합을 탐색합니다.  중복을 제거하기 위해 `final` 리스트에 중복되지 않은 조합만 저장합니다.  핵심은 이전에 선택된 수보다 큰 수만 선택하여 증가하는 수열을 생성하는 점과, 중복된 조합을 제거하여 출력하는 점입니다.


### 📝 **알고리즘**

1. **입력:** N과 M을 입력받습니다.
2. **재귀 함수 `make_num`:**
   - 기저 사례: M개의 수를 선택했으면 (`m == M`) 현재 `result` 리스트를 `last` 리스트에 추가하고 재귀를 종료합니다.
   - 재귀 단계: 1부터 N까지의 수를 순차적으로 검사합니다.
     - 만약 `result`가 비어있거나, 현재 선택된 마지막 수보다 큰 수이면 (`result[-1] < i+1`), 해당 수를 `result`에 추가하고 재귀적으로 `make_num` 함수를 호출합니다.
     - 재귀 호출 후에는 `result`에서 해당 수를 제거하여 다음 조합을 탐색합니다 (Backtracking).
3. **중복 제거:** `last` 리스트에 저장된 모든 조합 중 중복된 조합을 제거하여 `final` 리스트에 저장합니다.
4. **출력:** `final` 리스트에 저장된 조합들을 출력합니다.


### 🧐 **시간 복잡도**

`make_num` 함수는 N개의 수 중 M개를 선택하는 모든 경우의 수를 탐색합니다.  이는  `N! / (M! * (N-M)!)` 개의 조합이 존재하며, 최악의 경우 시간 복잡도는 O(N!)에 가깝습니다.  하지만 가지치기를 통해 모든 경우의 수를 탐색하지는 않으므로 실제 시간 복잡도는 O(N!) 보다는 작지만, M이 N에 비해 작지 않다면 여전히 지수 시간 복잡도를 가집니다. 중복 제거 과정에서 `in` 연산을 사용하지만,  `final` 리스트의 크기는 최대 `N! / (M! * (N-M)!)` 이므로, 이 부분의 시간복잡도는 전체 시간 복잡도에 비해 상대적으로 작습니다. 따라서 전체적인 시간 복잡도는  **O(N!)에 가깝습니다**.  N과 M의 크기에 따라 시간 복잡도가 급격히 증가할 수 있음을 의미합니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 15650: N과 M (2)
# https://www.acmicpc.net/problem/15650

def make_num(m, start):
    if m == M:
        last.append(result.copy())
        return
    
    
    for i in range(N):
        if not result:
            result.append(i+1)
            make_num(m+1, i+1)
            result.pop()
        else:
            if result[-1] < i+1:
                result.append(i+1)
                make_num(m+1, i+1)
                result.pop()




N, M = map(int,input().split())

last = []
result = []


visited = [False] * N
make_num(0,0)

final = []
for i in range(len(last)):
    if last[i] not in final:
        final.append(last[i])

for i in range(len(final)):
    print(*final[i])
</details>