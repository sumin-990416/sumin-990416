# 📝 Baekjoon 1969: DNA

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![실버 4](https://img.shields.io/badge/Silver-4-949393?style=for-the-badge) | `브루트포스 알고리즘` | [1969번 문제](https://www.acmicpc.net/problem/1969) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

문제는 주어진 DNA 서열들에서 각 위치별로 가장 많이 등장하는 염기(A, C, G, T)를 찾고, 그 염기를 결과 문자열에 추가하는 것입니다.  그리고 각 위치에서 가장 많이 등장하는 염기가 아닌 다른 염기의 개수를 합산하여 최종적으로 필요한 변환 횟수를 계산합니다.  즉, 각 열에서 가장 흔한 염기를 선택하고, 그 염기로 모든 DNA 서열을 맞추기 위해 필요한 변환 횟수를 구하는 것입니다.


### 📝 **알고리즘**

1. **입력:**  DNA 서열의 개수 `n`과 각 서열의 길이 `m`을 입력받습니다.  `n`개의 DNA 서열을 리스트 `list_dna`에 저장합니다.

2. **열별 최빈 염기 찾기:** 각 열(j)에 대해,  A, C, G, T의 개수를 `list_num` 리스트에 저장합니다.  `list_num`에서 가장 큰 값의 인덱스를 찾아 해당 염기를 결과 문자열 `result`에 추가합니다.

3. **변환 횟수 계산:**  각 열에서 가장 많은 염기가 아닌 다른 염기의 개수를 `result_n`에 누적합니다.

4. **출력:** 결과 문자열 `result`와 필요한 변환 횟수 `result_n`을 출력합니다.


### 🧐 **시간 복잡도**

- DNA 서열 입력: O(nm)
- 열별 최빈 염기 찾기 및 변환 횟수 계산: O(nm)
- 결과 출력: O(m)

따라서 전체 알고리즘의 시간 복잡도는 O(nm) 입니다.  n은 DNA 서열의 개수, m은 각 서열의 길이입니다.  입력 크기에 선형적으로 비례하는 시간 복잡도를 가집니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1969: DNA
# https://www.acmicpc.net/problem/1969

n, m = map(int,input().split())

result = ''
result_n = 0
list_dna = []
for _ in range(n):
    list_dna.append(input())


for j in range(m):
    list_num = [0,0,0,0]
    for i in range(n):
        if list_dna[i][j] == 'A':
            list_num[0] += 1
        if list_dna[i][j] == 'C':
            list_num[1] += 1
        if list_dna[i][j] == 'G':
            list_num[2] += 1
        if list_dna[i][j] == 'T':
            list_num[3] += 1
    
    idx = 0
    for i in range(4):
        if list_num[i] > list_num[idx]:
            idx = i
    result_n += n - list_num[idx]
    if idx == 0:
        result += 'A'
    if idx == 1:
        result += 'C'
    if idx == 2:
        result += 'G'
    if idx == 3:
        result += 'T'

print(result)
print(result_n)
</details>