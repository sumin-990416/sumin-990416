# 📝 Baekjoon 2309: 일곱 난쟁이

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-08 | ![브론즈 1](https://img.shields.io/badge/Bronze-1-B56A3C?style=for-the-badge) | `브루트포스 알고리즘` | [2309번 문제](https://www.acmicpc.net/problem/2309) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### 🧠 **핵심 아이디어**

9명의 키를 입력받아 7명을 선택하여 키의 합이 100이 되는 조합을 찾는 문제입니다.  비트마스킹을 이용하여 모든 가능한 7명의 조합을 효율적으로 생성하고, 합계가 100인 조합을 찾으면 반복문을 종료합니다.

### 📝 **알고리즘**

1. **입력:** 9명의 키를 입력받아 리스트 `list_num`에 저장합니다.
2. **정렬:** 입력받은 키 리스트를 오름차순으로 정렬합니다. 이는 출력을 위한 정렬일 뿐, 알고리즘의 핵심 로직에는 영향을 미치지 않습니다.
3. **비트마스킹:**  `1 << len(list_num)` 까지의 비트를 순회하며, 각 비트가 1인 경우 해당 인덱스의 키를 `num_list`에 추가합니다. 이는 9명 중 7명을 선택하는 모든 조합을 생성하는 방법입니다.  `i & (1 << idx)` 연산을 통해 특정 비트가 1인지 확인합니다.
4. **조건 확인:** `num_list`의 합이 100이고, 원소의 개수가 7인 경우, 해당 조합이 문제의 조건을 만족하는 것이므로 반복문을 `break`로 종료합니다.
5. **출력:** 찾은 `num_list`를 오름차순으로 정렬하여 각 키를 한 줄씩 출력합니다.


### 🧐 **시간 복잡도**

입력받은 숫자의 개수를 N이라고 하면 (N=9),  비트마스킹을 이용하여 모든 부분집합을 탐색하는 시간 복잡도는 O(2<sup>N</sup>) 입니다.  하지만 문제의 조건에 따라 7명을 선택해야 하므로 실제로는  O(N * <sub>N</sub>C<sub>7</sub>)  정도의 시간 복잡도를 가집니다.  N이 9로 고정되어 있으므로, 시간 복잡도는 상수 시간 O(1)으로 볼 수 있습니다. 정렬의 시간 복잡도는 O(N log N) 이지만, N이 작으므로 전체 시간 복잡도에 미치는 영향은 크지 않습니다.  전체적으로 매우 효율적인 알고리즘입니다.


<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 2309: 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

list_num = []

for i in range(9):
    list_num.append(int(input()))

list_num.sort()

for i in range(1<<len(list_num)):
    num_list = []
    for idx in range(len(list_num)):
        if i & (1<<idx):
            num_list.append(list_num[idx])
    if sum(num_list) == 100 and len(num_list) == 7:
        break

num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])
</details>