# 📝 Baekjoon 2407: 조합

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-04 | ![실버 3](https://img.shields.io/badge/Silver-3-949393?style=for-the-badge) | `수학` | [2407번 문제](https://www.acmicpc.net/problem/2407) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

이 코드는 nCm (n choose m), 즉 n개 중 m개를 선택하는 조합의 수를 계산하는 재귀 함수를 사용합니다.  분모와 분자를 따로 계산하여 나눗셈을 최대한 늦추는 방식으로, 큰 수를 다룰 때 발생할 수 있는 오버플로우 문제를 완화합니다.  `result_1`에 분자(n!), `result_2`에 분모(m! * (n-m)!)를 누적하여 계산합니다.


### 📝 **알고리즘**

`make_com(num, k)` 함수는 재귀적으로 조합을 계산합니다.

1. **기저 사례:** `k`가 `m+1`이 되면, `result_1 / result_2`를 출력하고 재귀를 종료합니다. 이는 분자와 분모를 모두 계산했음을 의미합니다.

2. **재귀 호출:** `result_1`에 `num`을 곱하고, `result_2`에 `k`를 곱합니다. 이는 분자와 분모에 해당하는 수를 누적하는 과정입니다.  그 후, `make_com(num-1, k+1)`을 호출하여 재귀적으로 계산을 진행합니다.  `num`은 선택 가능한 원소의 개수, `k`는 선택한 원소의 개수를 나타냅니다.


### 🧐 **시간 복잡도**

재귀 함수가 m번 호출됩니다. 각 호출에서 상수 시간의 연산만 수행되므로, 시간 복잡도는 O(m) 입니다.  하지만 실제로는 팩토리얼 계산의 숨겨진 비용이 있으므로,  정확하게는 O(m)에 가까운 시간 복잡도를 가진다고 볼 수 있습니다.  단순히 팩토리얼 연산 자체의 복잡도는 O(m)이지만, 큰 수를 다루기 위한 연산의 오버헤드는 무시할 수 없습니다.  하지만 입력 크기 n에 비례하는 복잡도는 아니므로, 상대적으로 효율적입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 2407: 조합
# https://www.acmicpc.net/problem/2407

n, m = map(int,input().split())

result_1 = 1
result_2 = 1
def make_com(num,k):
    global result_1,result_2
    if k == m+1:
        print(result_1//result_2)
        return    
    
    result_1 *= num
    result_2 *= k
    make_com(num-1,k+1)

make_com(n,1)
</details>