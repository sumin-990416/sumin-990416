# 📝 Baekjoon 5052: 전화번호 목록

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![골드 4](https://img.shields.io/badge/Gold-4-E5A323?style=for-the-badge) | `집합과 맵` | [5052번 문제](https://www.acmicpc.net/problem/5052) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

입력으로 주어진 문자열들을 사전순으로 정렬한 후, 인접한 문자열들을 비교하여 앞 문자열이 뒤 문자열의 접두어인지 확인하는 방식으로 문제를 해결합니다.  접두어 관계가 발견되면 사전순으로 정렬했음에도 불구하고, 접두사 관계가 존재하므로 순열을 만들 수 없다는 것을 의미합니다.


### 📝 **알고리즘**

1. **입력:** 테스트 케이스의 수 T와 각 테스트 케이스에 대한 문자열 개수 n, 그리고 n개의 문자열을 입력받습니다.
2. **정렬:** 입력받은 n개의 문자열들을 사전순으로 정렬합니다.
3. **접두어 확인:** 정렬된 문자열 리스트를 순회하며, 각 문자열과 그 다음 문자열을 비교합니다.  `startswith()` 메서드를 이용하여 앞 문자열이 뒤 문자열의 접두어인지 확인합니다.
4. **결과 판정:** 만약 접두어 관계가 발견되면 `result` 변수를 'NO'로 설정하고 반복문을 종료합니다. 접두어 관계가 발견되지 않으면 `result` 변수는 'YES'로 유지됩니다.
5. **출력:** `result` 변수의 값 ('YES' 또는 'NO')을 출력합니다.


### 🧐 **시간 복잡도**

- 문자열 정렬: `n`개의 문자열을 정렬하므로, 최악의 경우 O(n log n)의 시간 복잡도를 가집니다.  (사용하는 정렬 알고리즘에 따라 다를 수 있지만, 파이썬의 `sort()`는 일반적으로 Timsort를 사용하며 O(n log n)의 시간 복잡도를 가집니다.)
- 접두어 확인: 정렬된 문자열 리스트를 한 번 순회하므로 O(n)의 시간 복잡도를 가집니다.  `startswith()` 메서드는 O(k)의 시간 복잡도를 가지지만, k는 문자열의 길이로 입력 크기 n과 무관하게 볼 수 있으므로 상수 시간으로 간주할 수 있습니다.
- 따라서 전체 알고리즘의 시간 복잡도는 정렬 부분의 지배적인 영향으로 **O(n log n)**입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 5052: 전화번호 목록
# https://www.acmicpc.net/problem/5052

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = [input() for _ in range(n)]
    numbers.sort()
    
    result = 'YES'
    for i in range(n - 1):
        if numbers[i+1].startswith(numbers[i]):
            result = 'NO'
            break
            
    print(result)
</details>