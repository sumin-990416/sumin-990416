# 📝 Baekjoon 7568: 덩치

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-04 | ![실버 5](https://img.shields.io/badge/Silver-5-949393?style=for-the-badge) | `구현, 브루트포스 알고리즘` | [7568번 문제](https://www.acmicpc.net/problem/7568) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

주어진 `n`개의 (kg, cm) 쌍에 대해 각 쌍의 랭크를 계산하는 문제입니다.  특정 쌍의 랭크는 그 쌍보다 kg과 cm 모두 작은 쌍의 개수에 1을 더한 값입니다.  즉,  다른 모든 쌍과 비교하여 kg과 cm 모두 더 큰 쌍의 개수를 세어 순위를 결정합니다.

### 📝 **알고리즘**

1. **입력:** `n`과 `n`개의 (kg, cm) 쌍을 입력받아 `list_num` 리스트에 저장합니다.
2. **랭크 계산:** `find_rank` 함수는 주어진 (kg, cm) 쌍에 대해 다른 모든 쌍과 비교합니다.  `list_num`을 순회하며 현재 쌍보다 kg과 cm 모두 작은 쌍을 발견할 때마다 랭크를 1씩 증가시킵니다.  최종적으로 계산된 랭크를 반환합니다.
3. **결과 출력:** 입력받은 모든 쌍에 대해 `find_rank` 함수를 호출하여 각 쌍의 랭크를 계산하고, `result` 리스트에 저장합니다.  최종적으로 `result` 리스트의 원소들을 공백으로 구분하여 출력합니다.

### 🧐 **시간 복잡도**

`find_rank` 함수는 `n`개의 쌍을 순회하므로 O(n)의 시간 복잡도를 가집니다.  이 함수는 `n`번 호출되므로 전체 알고리즘의 시간 복잡도는 O(n*n) 즉, O(n²) 입니다.  중첩 반복문(nested loop) 구조로 인해 시간 복잡도가 제곱 시간에 비례합니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 7568: 덩치
# https://www.acmicpc.net/problem/7568

def find_rank(num1,num2):
    rank = 1
    for i in range(n):
        if num1 < list_num[i][0] and num2 < list_num[i][1]:
            rank += 1
    return rank



n = int(input())

list_num = []
for _ in range(n):
    kg,cm = map(int,input().split())
    list_num.append([kg,cm])

result = []
for i in range(n):
    kg_i, cm_i = list_num[i]
    result.append(find_rank(kg_i,cm_i))

print(*result)
</details>