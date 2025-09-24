# 📝 Baekjoon 2018: 수들의 합5

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-24 | ![실버 5](https://img.shields.io/badge/Silver-5-949393?style=for-the-badge) | `수학` | [2018번 문제](https://www.acmicpc.net/problem/2018) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

주어진 자연수 n에 대해, 연속된 자연수의 합으로 n을 표현할 수 있는 경우의 수를 구하는 문제입니다.  1부터 시작하는 연속된 자연수의 합을 계산하며, 그 합이 n과 같으면 경우의 수를 1 증가시키는 방식으로 문제를 해결합니다.


### 📝 **알고리즘**

`find_sum(n)` 함수는 입력값 n에 대해 연속된 자연수의 합으로 n을 만들 수 있는 경우의 수를 반환합니다.  

1. `result` 변수를 1로 초기화합니다. (n자체는 항상 연속된 자연수의 합으로 표현 가능하므로)
2. 1부터 n-1까지 반복하며(외부 루프), 각 i에 대해 연속된 자연수의 합을 계산합니다(내부 루프).
3. 내부 루프는 `j`를 `i`로 초기화하고, `num`에 연속된 자연수의 합을 누적합니다.  `num`이 n보다 작거나 같은 동안 `j`를 1씩 증가시키며 합을 계산합니다.
4. `num`이 n과 같다면, `result`를 1 증가시켜 경우의 수를 카운트합니다.
5. 최종적으로 `result`를 반환합니다.


### 🧐 **시간 복잡도**

외부 루프는 n-1번 반복하고, 내부 루프는 최악의 경우 O(n)번 반복합니다. 따라서 전체 시간 복잡도는 O(n²) 입니다.  입력 n의 크기에 따라 제곱의 시간이 걸리므로, 매우 큰 n에 대해서는 비효율적일 수 있습니다.  하지만 백준 문제의 입력 범위를 고려하면 충분히 효율적인 알고리즘입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 2018: 수들의 합5
# https://www.acmicpc.net/problem/2018

def find_sum(n):
    result = 1
    for i in range(1,n):
        j = i
        num = 0
        while num < n:
            num += j
            j += 1

        if num == n:
            result += 1

    return result


print(find_sum(int(input())))
</details>