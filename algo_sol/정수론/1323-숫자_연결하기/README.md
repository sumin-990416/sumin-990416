# 📝 Baekjoon 1323: 숫자 연결하기

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-24 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `정수론` | [1323번 문제](https://www.acmicpc.net/problem/1323) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

주어진 자연수 `n`에 대해,  `n`, `nn`, `nnn`, ...  과 같은 형태의 수를 k로 나눈 나머지가 0이 되는 최소 개수를 찾는 문제입니다.  나머지가 반복될 경우, 0이 될 수 없음을 알 수 있으므로,  나머지의 반복 여부를 확인하며 계산합니다.  핵심은 나머지를 저장하여 반복되는지 체크하는 것입니다.


### 📝 **알고리즘**

`make_mod(n, k)` 함수는 다음과 같은 과정을 거칩니다.

1. **초기값 설정:** `n`을 `k`로 나눈 나머지 `mod`를 구합니다. `mod`가 0이면 1을 반환합니다. (처음부터 나누어 떨어지는 경우)

2. **나머지 목록 생성 및 반복:** `mod`를 저장하는 집합 `mod_list`를 생성합니다.  `shift` 변수는 `n`의 자릿수만큼 10의 거듭제곱을 저장하여 다음 수를 생성하는 데 사용됩니다.  반복문을 통해 `mod`를 업데이트 합니다.  업데이트는 `mod * shift + n`을 `k`로 나눈 나머지를 구하는 방식으로 이루어집니다.  이는 `n`, `nn`, `nnn`, ... 의 형태의 수를 나타냅니다.

3. **반복 확인 및 종료:** 각 반복마다 `mod`가 0인지 확인하고, 0이면 현재 반복 횟수 `count`를 반환합니다.  만약 `mod`가 `mod_list`에 이미 존재한다면, 나머지가 반복되는 것이므로 -1을 반환하여 0이 될 수 없음을 나타냅니다.  `mod`를 `mod_list`에 추가하고 반복을 계속합니다.

4. **반복 최대 횟수:** `k`번의 반복 후에도 0이 되지 않으면 -1을 반환합니다. (나머지가 순환하지 않고 0이 되지 않는 경우)


### 🧐 **시간 복잡도**

최악의 경우, `k`번의 반복이 수행됩니다. 각 반복에서 집합 `mod_list`에 대한 삽입 및 탐색 연산이 수행되지만, 집합 연산은 평균적으로 O(1)의 시간 복잡도를 가지므로, 전체적인 시간 복잡도는 O(k) 입니다.  `k`가 입력의 크기이므로, 선형 시간 복잡도를 가집니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1323: 숫자 연결하기
# https://www.acmicpc.net/problem/1323

n, k = map(int, input().split())


def make_mod(n, k):
    mod = n % k
    if mod == 0:
        return 1

    mod_list = {mod}
    count = 1
    shift = 10 ** len(str(n))
    for _ in range(k):
        mod = (mod * shift + n) % k
        count += 1
        if mod == 0:
            return count

        if mod in mod_list:
            return -1
        mod_list.add(mod)
    return -1

result = make_mod(n, k)
print(result)
</details>