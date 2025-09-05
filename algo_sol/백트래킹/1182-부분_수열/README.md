# 📝 Baekjoon 1182: 부분 수열

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-05 | ![실버 2](https://img.shields.io/badge/Silver-2-949393?style=for-the-badge) | `백트래킹` | [1182번 문제](https://www.acmicpc.net/problem/1182) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

주어진 리스트 `list_num`에서 원소들의 부분집합 중 합이 `m`이 되는 부분집합의 개수를 찾는 문제입니다.  비트마스크를 이용하여 모든 부분집합을 효율적으로 생성하고, 각 부분집합의 합을 검사하여 조건을 만족하는 경우의 수를 셉니다.

### 📝 **알고리즘**

1. 입력으로 리스트의 크기 `n`과 목표 합 `m`을 받습니다.
2. 리스트 `list_num`을 입력받습니다.
3. `0`부터 `2^n - 1`까지의 정수를 순회하며, 각 정수를 비트마스크로 사용합니다.  각 비트는 리스트의 원소를 선택할지 여부를 나타냅니다. (0: 선택 안 함, 1: 선택)
4. 각 비트마스크에 대해, 해당 비트가 1인 원소들을 부분집합 `subset`에 추가합니다.
5. `subset`의 합이 `m`이고, `subset`이 공집합이 아닌 경우, `count_num`을 증가시킵니다.
6. 최종적으로 `count_num` (합이 m인 부분집합의 개수)을 출력합니다.


### 🧐 **시간 복잡도**

외부 루프는 0부터 2<sup>n</sup> -1 까지 반복하므로 O(2<sup>n</sup>)의 시간 복잡도를 가집니다. 내부 루프는 최대 n번 반복합니다.  따라서 전체 시간 복잡도는 O(n * 2<sup>n</sup>) 입니다.  n이 리스트의 크기이므로, 리스트의 크기가 커지면 지수적으로 시간이 증가합니다.  이는 부분집합 생성 문제의 본질적인 시간 복잡도입니다.


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