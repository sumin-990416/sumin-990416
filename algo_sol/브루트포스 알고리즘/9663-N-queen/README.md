# 📝 Baekjoon 9663: N-queen

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `브루트포스 알고리즘` | [9663번 문제](https://www.acmicpc.net/problem/9663) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

N-Queen 문제를 재귀 함수를 이용하여 해결하는 코드입니다.  `able(x)` 함수는 x번째 행에 퀸을 놓았을 때, 이전에 놓인 퀸들과 공격 가능한 위치에 있는지 확인합니다. `queen(x)` 함수는 x번째 행부터 순차적으로 퀸을 배치하며, 모든 행에 퀸을 배치할 수 있는 경우의 수를 센 후 결과를 출력합니다.  핵심은 백트래킹(Backtracking) 기법을 사용하여 가능한 모든 경우를 탐색하며, 충돌이 발생하면 이전 상태로 돌아가 다른 경우를 시도하는 것입니다.


### 📝 **알고리즘**

1. **`able(x)` 함수:**  x번째 행에 퀸을 놓을 위치를 검사합니다.  같은 열(`row[x] == row[i]`) 또는 대각선(`abs(row[x] - row[i]) == abs(x - i)`)에 이미 퀸이 있는 경우 `False`를 반환하여 충돌을 감지합니다.  충돌이 없으면 `True`를 반환합니다.

2. **`queen(x)` 함수:** 재귀 함수로, x번째 행에 퀸을 배치하는 역할을 합니다.
    - 기저 사례: x가 n과 같으면 (모든 행에 퀸을 배치했으면) `result` (해의 개수)를 1 증가시키고 종료합니다.
    - 재귀 단계: 0부터 n-1까지의 열에 퀸을 배치해보며 (`row[x] = i`), `able(x)` 함수를 통해 충돌이 없는지 검사합니다. 충돌이 없으면 다음 행 (`x+1`)에 대한 `queen(x+1)` 함수를 재귀적으로 호출합니다.

3. **메인 부분:** 입력으로 체스판 크기 n을 받고, `row` 리스트를 초기화합니다.  `result` 변수를 0으로 초기화하고, `queen(0)` 함수를 호출하여 재귀적으로 해를 찾습니다. 마지막으로 `result` 값 (해의 개수)을 출력합니다.


### 🧐 **시간 복잡도**

시간 복잡도는 O(n!)입니다.  최악의 경우, 모든 행에 대해 모든 열을 시도해야 하므로, n개의 행에 대해 n개의 선택지를 가지는 순열을 모두 탐색하게 됩니다.  따라서 시간 복잡도는 n!에 비례합니다.  이는 백트래킹 알고리즘의 특징으로, 모든 가능한 경우의 수를 탐색하기 때문에 지수 시간 복잡도를 가집니다.  n이 커질수록 계산 시간이 기하급수적으로 증가합니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 9663: N-queen
# https://www.acmicpc.net/problem/9663

def able(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def queen(x):
    global result
    if x == n:
        result += 1
        return

    for i in range(n):
        row[x] = i
        if able(x):
            queen(x+1)

n = int(input())
row = [0] * n

result = 0
queen(0)
print(result)
</details>