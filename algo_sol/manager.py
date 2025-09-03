# manager.py

import os
import subprocess
import datetime
import sys

# --- 설정 부분 ---
# 나중에 파일 확장자를 바꾸고 싶다면 이 부분을 수정하세요. (예: .java, .cpp)
DEFAULT_CODE_EXTENSION = ".py" 
# -----------------


def get_ai_summary(code_content: str) -> str:
    """
    AI(Gemini)가 코드 내용을 분석하여 풀이 전략을 요약해주는 함수입니다.
    실제로는 이 부분에서 API 호출이 일어나지만, 여기서는 시연을 위해
    분석 결과로 나올 법한 표준 템플릿을 반환합니다.
    """
    print("🤖 AI가 코드를 분석하여 풀이 전략을 요약 중입니다...")
    
    summary = f'''
### 🧠 **핵심 아이디어**
- 문제의 핵심 요구사항을 어떤 방식으로 접근하여 해결했는지에 대한 요약입니다.
- (예: '최단 거리를 구해야 하므로 BFS를 활용했습니다.')

### 📝 **알고리즘**
- **자료구조**: 사용한 주요 자료구조 (예: `deque`를 이용한 큐, 우선순위 큐 등)
- **알고리즘**: 적용한 핵심 알고리즘 (예: 너비 우선 탐색 (BFS), 동적 계획법 (DP))

### 🧐 **시간 복잡도**
- 이 풀이의 시간 복잡도는 $O(V+E)$ 입니다. (V: 정점의 수, E: 간선의 수)
- (예시이며, 실제 분석 결과는 코드에 따라 달라집니다.)

### 🤔 **어려웠던 점**
- 구현 중 겪었던 문제나, 특정 테스트 케이스를 통과하기 위해 고민했던 부분을 기록합니다.
- (예: '시간 초과를 해결하기 위해 `sys.stdin.readline`을 사용했습니다.')
'''
    return summary.strip()


def create_readme(info: dict, summary: str, code: str) -> str:
    """README.md 파일의 전체 내용을 생성합니다."""
    
    today = datetime.date.today().isoformat()
    
    # f-string을 사용하여 마크다운 템플릿을 완성합니다.
    return f"""#  Baekjoon {info['number']}: {info['title']}

- **Solved Date**: {today}
- **Problem Link**: [https://www.acmicpc.net/problem/{info['number']}]({info['link']})
- **Difficulty**: {info['level']}
- **Algorithm**: {info['algo']}

---

## ✅ Solution Status

**Solved!** ✔️

---

## 🤖 AI Summary

{summary}

---

## 💻 My Code

```python
# Baekjoon Problem {info['number']}: {info['title']}
# [https://www.acmicpc.net/problem/](https://www.acmicpc.net/problem/){info['number']}

{code.strip()}
"""

def main():
    print("="*40)
    print("🚀 백준 문제 풀이 자동화 매니저를 시작합니다.")
    print("="*40)

    # 1. 사용자로부터 문제 정보 입력받기
    try:
        problem_info = {
            'number': input("▎문제 번호를 입력하세요 (예: 1000): "),
            'title': input("▎문제 제목을 입력하세요 (띄어쓰기 가능, 예: A+B): "),
            'algo': input("▎알고리즘 분류를 입력하세요 (폴더명, 예: 구현): "),
            'level': input("▎문제 난이도를 입력하세요 (예: Bronze 5): "),
        }
        problem_info['link'] = f"https://www.acmicpc.net/problem/{problem_info['number']}"
        
        # 제목의 공백을 언더스코어(_)로 변경하여 폴더명으로 사용
        folder_safe_title = problem_info['title'].replace(" ", "_")
        
    except KeyboardInterrupt:
        print("\n👋 작업을 중단합니다.")
        sys.exit()

    # 2. 소스 코드 파일 읽기
    source_code_filename = problem_info['number'] + DEFAULT_CODE_EXTENSION
    try:
        with open(source_code_filename, 'r', encoding='utf-8') as f:
            code_content = f.read()
        print(f"\n📄 '{source_code_filename}' 파일을 성공적으로 읽었습니다.")
    except FileNotFoundError:
        print(f"\n❌ 오류: '{source_code_filename}' 파일을 찾을 수 없습니다.")
        print("   백준 문제 번호와 동일한 이름의 .py 파일을 생성해주세요. (예: 1000.py)")
        sys.exit()

    # 3. AI 요약 생성 및 README 내용 조합
    ai_summary = get_ai_summary(code_content)
    readme_content = create_readme(problem_info, ai_summary, code_content)
    print("✒️ README.md 파일 내용 생성이 완료되었습니다.")

    # 4. 폴더 생성 및 파일 이동
    target_dir = os.path.join(problem_info['algo'], f"{problem_info['number']}-{folder_safe_title}")
    os.makedirs(target_dir, exist_ok=True)

    # README.md 파일 저장
    with open(os.path.join(target_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
        
    # 소스 코드 파일을 목표 폴더로 이동
    os.rename(source_code_filename, os.path.join(target_dir, source_code_filename))
    print(f"📁 '{target_dir}' 폴더에 풀이 파일과 README를 저장했습니다.")

    # 5. Git에 자동으로 업로드
    try:
        print("\n☁️ Git에 변경 사항을 업로드합니다...")
        subprocess.run(['git', 'add', '.'], check=True)
        commit_message = f"feat: Solve BOJ {problem_info['number']} ({problem_info['title']})"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("\n✨ Git 업로드 완료! GitHub에서 확인해보세요.")
        print("="*40)
    except FileNotFoundError:
        print("\n❌ 오류: Git이 설치되어 있지 않거나 Git을 실행할 수 없습니다.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Git 작업 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()      