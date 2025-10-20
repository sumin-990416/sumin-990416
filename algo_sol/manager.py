# manager.py (보안 강화 최종 버전)
import datetime
import os
import sys
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
# 1. 환경 변수에서 API 키를 안전하게 불러옵니다.
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. 지원할 프로그래밍 언어의 파일 확장자 목록입니다.
SUPPORTED_EXTENSIONS = [".py", ".java", ".cpp", ".js", ".kt"]


def analyze_code_with_gemini(code_content: str, language: str) -> str:
    """Gemini API를 호출하여 코드 분석을 요청하고, 그 결과를 받아오는 함수."""
    print("🤖 Gemini AI가 코드를 실시간으로 분석 중입니다... (최신 모델: gemini-flash-lite-latest)")
    
    try:
        genai.configure(api_key=API_KEY)
        # <<< 모델을 최신 버전으로 변경 >>>
        model = model = genai.GenerativeModel('gemini-flash-lite-latest')
        
        # AI에게 내릴 구체적인 명령 (프롬프트)
        prompt = f"""
        당신은 백준 알고리즘 풀이 분석 전문가입니다.
        아래 {language} 코드는 백준 온라인 저지 문제의 정답 코드입니다.
        코드를 분석해서 다음 항목에 대해 한국어 마크다운 형식으로 설명해주세요.

        - ### 🧠 **핵심 아이디어**
        - ### 📝 **알고리즘**
        - ### 🧐 **시간 복잡도**

        '어려웠던 점' 항목은 제외하고, 전문가처럼 간결하고 정확하게 설명해주세요.

        ---
        [분석할 코드]
        ```{language}
        {code_content}
        ```
        ---
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"### ❌ AI 분석 실패\n- 오류: {e}\n- API 키가 정확한지, 환경 변수 설정이 올바르게 되었는지 확인해주세요."


# ... (create_readme 함수와 main 함수 나머지 부분은 이전과 동일합니다) ...
# ... (이전 답변의 나머지 함수 코드를 여기에 붙여넣으세요) ...

# manager.py 파일의 이 함수만 교체하면 됩니다.

def create_readme(info: dict, summary: str, code: str) -> str:
    """README.md 파일의 전체 내용을 생성합니다. (디자인 개선 버전)"""
    
    # --- 난이도 뱃지 생성 로직 ---
    # 난이도 문자열(예: "Silver 4")을 공백으로 분리
    try:
        tier, level = info['level'].replace("실버", "Silver").replace("골드", "Gold").replace("브론즈", "Bronze").split()
        # 뱃지 색상 맵
        color_map = {
            "Bronze": "B56A3C",
            "Silver": "949393",
            "Gold": "E5A323",
            "Platinum": "52E2A8",
            "Diamond": "48A5FF",
            "Ruby": "FF537E"
        }
        badge_color = color_map.get(tier, "lightgrey")
        # 뱃지 이미지 URL 생성
        badge = f"![{info['level']}](https://img.shields.io/badge/{tier}-{level}-{badge_color}?style=for-the-badge)"
    except Exception:
        # 난이도 파싱 실패 시 기본 텍스트 뱃지
        badge = f"![{info['level']}](https://img.shields.io/badge/Difficulty-{info['level'].replace(' ', '%20')}-lightgrey?style=for-the-badge)"
    # --- 뱃지 생성 로직 끝 ---

    # f-string의 들여쓰기 문제를 해결하고, 새로운 레이아웃을 적용
    return f"""# 📝 Baekjoon {info['number']}: {info['title']}

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| {info['date']} | {badge} | `{info['algo']}` | [{info['number']}번 문제]({info['link']}) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

{summary}

<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````{info['language']}
# Baekjoon Problem {info['number']}: {info['title']}
# {info['link']}

{code.strip()}
</details>
"""

def main():
    """스크립트의 메인 실행 함수입니다."""
    print("="*40)
    print("🚀 백준 풀이 자동 분석 및 업로드 매니저")
    print("="*40)

    try:
        problem_number = input("▎문제 번호를 입력하세요: ")
        problem_title = input("▎문제 제목을 입력하세요: ")
        problem_level = input("▎문제 난이도를 입력하세요: ")
        problem_algo = input("▎알고리즘 분류를 입력하세요: ")

        problem_info = {
            'number': problem_number,
            'title': problem_title,
            'level': problem_level,
            'algo': problem_algo,
            'link': f"https://www.acmicpc.net/problem/{problem_number}",
            'date': datetime.date.today().isoformat(),  # 오늘 날짜로 기록
            'language': "unknown"
        }
        folder_safe_title = problem_info['title'].replace(" ", "_")
        
    except KeyboardInterrupt:
        print("\n👋 작업을 중단합니다."); sys.exit()

    source_code_filename = None
    for ext in SUPPORTED_EXTENSIONS:
        if os.path.exists(problem_number + ext):
            source_code_filename = problem_number + ext
            problem_info['language'] = ext.replace(".", "")
            break
            
    if not source_code_filename:
        print(f"\n❌ 오류: '{problem_number}'번 문제의 소스 코드 파일을 찾을 수 없습니다."); sys.exit()
        
    with open(source_code_filename, 'r', encoding='utf-8') as f:
        code_content = f.read()
    print(f"\n📄 '{source_code_filename}' 파일을 찾았습니다.")

    # API를 통해 AI 분석을 직접 실행
    ai_summary = analyze_code_with_gemini(code_content, problem_info['language'])

    readme_content = create_readme(problem_info, ai_summary, code_content)

    target_dir = os.path.join(problem_info['algo'], f"{problem_info['number']}-{folder_safe_title}")
    os.makedirs(target_dir, exist_ok=True)

    with open(os.path.join(target_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content.strip())

    os.rename(source_code_filename, os.path.join(target_dir, source_code_filename))
    print(f"\n📁 '{target_dir}' 폴더에 분석 결과와 코드를 저장했습니다.")

    # Git 업로드
    try:
        print("\n☁️ Git에 변경 사항을 업로드합니다...")
        subprocess.run(['git', 'add', '.'], check=True)
        commit_message = f"feat: Solve BOJ {problem_info['number']} ({problem_info['title']})"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("\n✨ Git 업로드 완료!")
        print("="*40)
    except Exception as e:
        print(f"\n❌ Git 작업 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # <<< 개선된 부분: 스크립트 실행 시 API 키가 설정되었는지 먼저 확인 >>>
    if not API_KEY:
        print("="*50)
        print("❌ 오류: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
        print("   스크립트를 실행하기 전에 API 키를 환경 변수로 설정해주세요.")
        print("="*50)
    else:
        main()