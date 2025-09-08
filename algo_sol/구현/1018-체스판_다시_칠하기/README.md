# 📝 Baekjoon 1018: 체스판 다시 칠하기

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-08 | ![실버3](https://img.shields.io/badge/Difficulty-실버3-lightgrey?style=for-the-badge) | `구현` | [1018번 문제](https://www.acmicpc.net/problem/1018) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

8x8 체스판에서 시작점의 색깔에 따라 'B' 또는 'W'로 시작하는 체스판을 만들었을 때,  주어진 체스판과의 차이(색깔이 다른 칸의 개수)를 최소화하는 방법을 찾는 문제입니다.  주어진 체스판의 8x8 부분 체스판을 순회하며, 각 부분 체스판에 대해 'B'로 시작하는 체스판과 'W'로 시작하는 체스판을 만들었을 때 색깔이 다른 칸의 개수를 계산합니다. 그 중 최솟값을 출력합니다.


### 📝 **알고리즘**

1. **입력:**  `n`과 `m` (체스판의 크기), 그리고 `n`개의 문자열로 이루어진 체스판 `board`를 입력받습니다.

2. **탐색:**  8x8 크기의 부분 체스판을 탐색하기 위해 `n-7` 행과 `m-7` 열을 반복문으로 순회합니다.

3. **색깔 비교:** 각 8x8 부분 체스판에 대해 'B'로 시작하는 체스판과 'W'로 시작하는 체스판 각각과의 차이를 계산합니다.  `(x+y)%2 == 0`을 이용하여 짝수 좌표와 홀수 좌표를 구분하고, 해당 좌표의 색깔이 기준 색깔과 다르면 카운트를 증가시킵니다.

4. **최솟값 찾기:** 모든 8x8 부분 체스판에 대한 두 가지 경우의 차이값을 `result` 리스트에 저장하고, 최솟값을 찾아 출력합니다.


### 🧐 **시간 복잡도**

시간 복잡도는 O(nm) 입니다.  `n-7`과 `m-7`을 반복하는 이중 for 루프에서 8x8 부분 체스판을 순회하며 비교하는 연산이 지배적입니다.  n과 m이 체스판의 행과 열의 크기이므로, 전체적으로 입력 크기에 비례하는 시간이 걸립니다.  내부 루프의 상수 시간 연산(8x8 비교)은 시간 복잡도에 영향을 미치지 않습니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1018: 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

n,m = map(int,input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        result1 = 0
        result2 = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) %2 == 0:
                    if board[x][y] != 'B':
                        result1 += 1
                    if board[x][y] != 'W':
                        result2 += 1
                else:
                    if board[x][y] != 'W':
                        result1 += 1
                    if board[x][y] != 'B':
                        result2 += 1
        result.append(result1)
        result.append(result2)

print(min(result))
</details>