# 📝 Baekjoon 15649: N과 M (1)

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-04 | ![실버 3](https://img.shields.io/badge/Silver-3-949393?style=for-the-badge) | `백트래킹` | [15649번 문제](https://www.acmicpc.net/problem/15649) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

백트래킹(Backtracking) 알고리즘을 이용하여 1부터 N까지의 수 중에서 M개의 수를 중복 없이 선택하는 모든 경우의 수를 출력하는 코드입니다.  재귀 함수 `make_num`을 통해 M개의 수를 순차적으로 선택하고, 선택된 수는 `result` 리스트에 저장합니다.  모든 조합을 탐색한 후에는 `result` 리스트에서 선택된 수를 제거(pop)하여 다음 조합을 탐색할 수 있도록 합니다.


### 📝 **알고리즘**

1. **입력:** N(1부터 N까지의 수)과 M(선택할 수의 개수)을 입력받습니다.
2. **재귀 함수 `make_num(m)`:**
   - `m`은 현재까지 선택된 수의 개수를 나타냅니다.
   - `m`이 `M`과 같으면 (M개의 수를 선택했으면) `result` 리스트에 저장된 수들을 출력하고 함수를 종료합니다.
   - `m`이 `M`보다 작으면 1부터 N까지의 수를 순회합니다.
   - 현재 수 `i+1`이 `result` 리스트에 이미 있는지 확인합니다.  중복을 허용하지 않기 위함입니다.
   - `result` 리스트에 `i+1`을 추가하고 재귀적으로 `make_num(m+1)`을 호출합니다.
   - 재귀 호출이 끝나면 `result` 리스트에서 `i+1`을 제거(pop)하여 다른 조합을 탐색할 수 있도록 합니다. (백트래킹)
3. **`make_num(0)` 호출:**  초기값 `m=0`으로 재귀 함수를 호출하여 알고리즘을 시작합니다.


### 🧐 **시간 복잡도**

시간 복잡도는 선택할 수의 개수(M)와 선택할 수 있는 범위(N)에 따라 결정됩니다.  N개의 수 중에서 M개를 순서를 고려하여 선택하는 경우의 수는  N! / (N-M)!  입니다.  알고리즘은 이 모든 경우의 수를 탐색하므로 시간 복잡도는 O(N! / (N-M)!) 입니다.  M이 N에 가까워질수록 시간 복잡도가 기하급수적으로 증가합니다.  이는  M과 N의 값이 작지 않을 경우 비효율적일 수 있음을 의미합니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 15649: N과 M (1)
# https://www.acmicpc.net/problem/15649

N, M = map(int,input().split())

result = []
def make_num(m):
    if m == M:
        print(*result)
        return
    for i in range(N):
        if (i + 1) in result:
            continue
        else:
            result.append(i+1)
            make_num(m+1)
            result.pop()


make_num(0)
</details>