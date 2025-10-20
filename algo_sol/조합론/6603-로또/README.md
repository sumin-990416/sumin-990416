# 📝 Baekjoon 6603: 로또

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-10-20 | ![실버 2](https://img.shields.io/badge/Silver-2-949393?style=for-the-badge) | `조합론` | [6603번 문제](https://www.acmicpc.net/problem/6603) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### ❌ AI 분석 실패
- 오류: 404 models/gemini-1.5-flash-latest is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.
- API 키가 정확한지, 환경 변수 설정이 올바르게 되었는지 확인해주세요.

<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 6603: 로또
# https://www.acmicpc.net/problem/6603

from itertools import combinations
n_list = []
while True:
    num_list = list(map(int,input().split()))
    n = num_list[0]
    if n == 0:
        break
    num = num_list[1:]
    num.sort()
    n_list.append(num)

for i in range(len(n_list)):
    comb = list(combinations(n_list[i],6))
    for com in comb:
        print(*com)
    print()
</details>