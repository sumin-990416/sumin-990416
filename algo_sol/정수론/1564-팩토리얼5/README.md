# 📝 Baekjoon 1564: 팩토리얼5

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-24 | ![실버 1](https://img.shields.io/badge/Silver-1-949393?style=for-the-badge) | `정수론` | [1564번 문제](https://www.acmicpc.net/problem/1564) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

입력받은 정수 N의 팩토리얼을 계산하고, 그 결과의 마지막 5자리를 출력하는 문제입니다.  단순히 팩토리얼을 계산하면 값이 매우 커지므로, 계산 과정에서 10으로 나누어지는 만큼 0을 제거하고,  `MOD`를 이용하여  계산 결과를 10<sup>12</sup>로 나눈 나머지를 계속해서 유지하며 연산량을 줄입니다.  최종적으로는 결과의 마지막 5자리만 출력합니다.

### 📝 **알고리즘**

1. **입력:** 표준 입력으로 정수 N을 받습니다.
2. **팩토리얼 계산 및 0 제거:** 1부터 N까지의 곱(팩토리얼)을 계산합니다. 계산 중에 10으로 나누어 떨어지는 만큼(0이 붙은 만큼) `fact`를 10으로 나누어 줍니다. 이는 0의 개수를 줄여 계산량을 효율적으로 줄이기 위함입니다.
3. **MOD 연산:**  계산 과정에서 `fact`를  `MOD` (10<sup>12</sup>)로 나눈 나머지만을 저장하여, 값이 지나치게 커지는 것을 방지합니다.
4. **마지막 5자리 추출:** 최종적으로 계산된 `fact`를 100000으로 나눈 나머지를 구하고,  `f"{result:05d}"`를 이용하여 5자리 숫자로 출력 형식을 맞춥니다.  만약 5자리보다 작다면 앞에 0을 채워 5자리로 만들어 출력합니다.
5. **출력:** 결과를 표준 출력으로 출력합니다.


### 🧐 **시간 복잡도**

N의 크기가 입력의 제한에 따라 달라지겠지만,  팩토리얼 계산 루프가 N번 반복되므로 시간 복잡도는 O(N)입니다.  `while` 루프는 0을 제거하는 과정이며,  0의 개수는 N이 커질수록 증가하지만,  `MOD` 연산으로 인해 전체 시간 복잡도에 미치는 영향은 미미합니다. 따라서 전체적인 시간 복잡도는 선형 시간 복잡도 O(N)으로 볼 수 있습니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1564: 팩토리얼5
# https://www.acmicpc.net/problem/1564

import sys


def factorial_five(n):
    fact = 1
    MOD = 10 ** 12

    for i in range(1, n + 1):

        fact *= i

        while fact % 10 == 0:
            fact //= 10
        fact %= MOD
    result = fact % 100000
    return f"{result:05d}"


N = int(sys.stdin.readline())

print(factorial_five(N))
</details>