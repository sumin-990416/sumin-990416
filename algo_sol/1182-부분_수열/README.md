# 📝 Baekjoon 1182: 부분 수열

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-05 | ![실버 2](https://img.shields.io/badge/Silver-2-949393?style=for-the-badge) | `` | [1182번 문제](https://www.acmicpc.net/problem/1182) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

주어진 숫자 리스트에서 부분집합을 생성하여 그 합이 m이 되는 부분집합의 개수를 구하는 문제입니다. 비트마스킹을 이용하여 모든 가능한 부분집합을 효율적으로 생성합니다.  각 숫자의 포함 여부를 비트로 표현하여 부분집합을 만들고, 합계를 계산합니다.


### 📝 **알고리즘**

1. **입력:** 정수 n과 m, 그리고 n개의 정수를 포함하는 리스트 `list_num`을 입력받습니다.
2. **비트마스킹:** 0부터 2<sup>n</sup> - 1까지의 정수를 순회합니다. 각 정수는 n개의 숫자에 대한 부분집합을 나타내는 비트마스크로 해석됩니다.  (i의 j번째 비트가 1이면 `list_num[j]`가 부분집합에 포함됨)
3. **부분집합 생성:** 비트마스크를 이용하여 부분집합 `subset`을 생성합니다.  `i & (1<<j)` 연산으로 j번째 비트가 1인지 확인합니다.
4. **합 계산 및 개수 증가:** 생성된 `subset`의 합을 계산합니다. 합이 m과 같고, 부분집합이 비어있지 않다면 (`subset`이 빈 리스트가 아닌 경우) `count_num`을 1 증가시킵니다.
5. **출력:** `count_num` (합이 m인 부분집합의 개수)를 출력합니다.


### 🧐 **시간 복잡도**

외부 루프는 0부터 2<sup>n</sup> - 1까지 반복되므로 O(2<sup>n</sup>)의 시간 복잡도를 가집니다. 내부 루프는 최대 n번 반복됩니다. 부분집합의 합을 계산하는 데는 최대 n번의 덧셈 연산이 필요합니다. 따라서 전체 시간 복잡도는 O(n * 2<sup>n</sup>) 입니다.  n이 작은 경우에는 효율적이지만, n이 커지면 지수적으로 증가하는 시간 복잡도를 가집니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1182: 부분 수열
# https://www.acmicpc.net/problem/1182

n, m = map(int,input().split())

list_num = list(map(int,input().split()))


count_num = 0
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(list_num[j])
    if sum(subset) == m and subset:
        count_num += 1

print(count_num)
</details>