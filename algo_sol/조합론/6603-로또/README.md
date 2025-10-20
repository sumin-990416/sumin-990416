# 📝 Baekjoon 6603: 로또

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-10-20 | ![실버 2](https://img.shields.io/badge/Silver-2-949393?style=for-the-badge) | `조합론` | [6603번 문제](https://www.acmicpc.net/problem/6603) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

다음은 백준 알고리즘 문제 풀이 코드에 대한 분석입니다.

---

### 🧠 **핵심 아이디어**

주어진 여러 숫자들 중에서 정확히 6개의 숫자를 뽑는 모든 가능한 조합(Combination)을 찾아 출력하는 것이 핵심입니다. 파이썬의 `itertools` 모듈에 포함된 `combinations` 함수를 사용하면 이 과정을 매우 효율적으로 처리할 수 있습니다.

### 📝 **알고리즘**

1.  **입력 처리**:
    *   프로그램은 `0`이 첫 번째 숫자로 입력될 때까지 반복하여 숫자 리스트를 입력받습니다.
    *   각 줄에서 첫 번째 숫자 `n`은 뒤이어 나오는 숫자의 개수를 나타내며, 이 `n`은 실제 조합을 만들 숫자 리스트에는 포함되지 않습니다.
    *   `num_list[1:]`를 통해 실제 조합을 만들 숫자들을 추출하고, `sort()`를 사용하여 오름차순으로 정렬합니다. (조합 결과의 일관성을 위함)
    *   정렬된 숫자 리스트들을 `n_list`에 저장합니다.

2.  **조합 생성 및 출력**:
    *   `n_list`에 저장된 각 숫자 리스트에 대해 반복합니다.
    *   `itertools.combinations(리스트, 6)` 함수를 사용하여 현재 리스트에서 6개의 숫자를 선택하는 모든 고유한 조합을 생성합니다.
    *   생성된 각 조합(`com`)을 언패킹(`*com`)하여 공백으로 구분된 형태로 출력합니다.
    *   하나의 입력 세트에 대한 모든 조합 출력이 끝나면, 다음 세트와의 구분을 위해 빈 줄을 출력합니다.

### 🧐 **시간 복잡도**

*   **입력 처리**: 각 테스트 케이스마다 `k`개의 숫자를 읽고 `k log k` 시간으로 정렬합니다. `M`개의 테스트 케이스가 있고 최대 `k_max`개의 숫자가 주어진다면, 이 부분은 대략 `O(M * k_max log k_max)`가 됩니다.
*   **조합 생성 및 출력**: 핵심적인 시간 소모는 `itertools.combinations` 함수가 `k`개의 숫자 중에서 6개를 선택하는 조합을 생성하는 부분입니다. `k`개 중에서 `r`개를 선택하는 조합의 수는 이항 계수 `C(k, r)`로 표현됩니다. 이 문제에서는 `r=6`이므로, 각 테스트 케이스당 `C(k, 6)`개의 조합이 생성됩니다.
    *   `C(k, 6) = k * (k-1) * (k-2) * (k-3) * (k-4) * (k-5) / (6 * 5 * 4 * 3 * 2 * 1)` 입니다.
    *   각 조합은 6개의 숫자로 이루어져 있으므로, 이를 출력하는 데 걸리는 시간은 상수 시간(6번의 출력)입니다.
    *   따라서, 하나의 테스트 케이스에 대한 조합 생성 및 출력 시간 복잡도는 `O(C(k, 6))` 또는 `O(k^6)`으로 볼 수 있습니다.
*   **총 시간 복잡도**: 전체 시간 복잡도는 `M`개의 테스트 케이스에 대해 `O(M * (k_max log k_max + C(k_max, 6)))`가 됩니다. 실제 `k`의 범위(보통 7 ≤ k ≤ 13)에서 `C(k, 6)`의 값은 상대적으로 작으므로, 매우 효율적으로 동작합니다. 예를 들어 `k=13`일 때 `C(13, 6) = 1716`입니다. `k log k` 부분보다 `C(k, 6)` 부분이 더 지배적입니다.

결론적으로, 이 코드의 시간 복잡도는 `O(M * k_max^6)` 또는 더 정확하게 `O(M * C(k_max, 6))`로 평가할 수 있습니다.

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