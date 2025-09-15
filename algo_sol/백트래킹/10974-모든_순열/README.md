# 📝 Baekjoon 10974: 모든 순열

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![실버 3](https://img.shields.io/badge/Silver-3-949393?style=for-the-badge) | `백트래킹` | [10974번 문제](https://www.acmicpc.net/problem/10974) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

주어진 n개의 숫자(1부터 n까지)에 대해 모든 순열(permutation)을 생성하여 출력하는 문제입니다.  `itertools` 라이브러리의 `permutations` 함수를 이용하여 효율적으로 모든 순열을 생성합니다.

### 📝 **알고리즘**

1. 입력으로 정수 n을 받습니다.
2. 1부터 n까지의 정수를 담은 리스트 `num_list`를 생성합니다.
3. `itertools.permutations(num_list, n)` 함수를 사용하여 `num_list`의 모든 n개의 순열을 생성합니다.  `permutations(iterable, r)` 함수는 iterable 객체에서 r개의 원소를 뽑아 순서를 고려하여 만들 수 있는 모든 순열을 생성합니다.  여기서는 n개의 원소를 모두 사용하므로 `n`을 두 번째 인자로 전달합니다.
4. 생성된 각 순열을 `print(*i)`를 이용하여 공백을 구분자로 하여 출력합니다.  `*i`는 순열 리스트 `i`를 unpacking하여 각 원소를 개별적으로 출력하는 것을 의미합니다.

### 🧐 **시간 복잡도**

`itertools.permutations` 함수는 n개의 원소에 대한 모든 순열을 생성하므로 시간 복잡도는 O(n!) 입니다.  n!은 n의 계승을 의미하며, n이 커짐에 따라 기하급수적으로 증가합니다. 따라서 n이 크다면 실행 시간이 매우 길어질 수 있습니다.  입출력 시간은 고려하지 않았습니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 10974: 모든 순열
# https://www.acmicpc.net/problem/10974

from itertools import permutations

n = int(input())

num_list = [i+1 for i in range(n)]

for i in permutations(num_list,n):
    print(*i)
</details>