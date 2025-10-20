# test_gemini_api.py
import os
import sys

try:
    import google.generativeai as genai
    print("✅ google-generativeai 패키지가 설치되어 있습니다.")
except ImportError:
    print("❌ google-generativeai 패키지가 설치되지 않았습니다.")
    print("💡 다음 명령어로 설치하세요: pip install google-generativeai")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ python-dotenv 패키지가 설치되어 있습니다. (.env 파일 로드 시도)")
except ImportError:
    print("⚠️  python-dotenv가 설치되지 않았습니다. 시스템 환경 변수만 확인합니다.")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("\n❌ GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
    sys.exit(1)

print(f"✅ API 키를 찾았습니다: {API_KEY[:10]}...{API_KEY[-4:]}")

print("\n🔄 Gemini API 연결을 테스트합니다...\n")

try:
    genai.configure(api_key=API_KEY)
    print("✅ API 키 설정 완료")
    
    print("\n📋 사용 가능한 모델 목록:")
    models = genai.list_models()
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
    
    # 🔥 최신 모델로 변경
    print("\n🧪 간단한 테스트 요청을 보냅니다...")
    model = genai.GenerativeModel('gemini-2.5-flash')  # 또는 'gemini-2.0-flash'
    response = model.generate_content("Hello! Please respond with 'API test successful!'")
    
    print("\n✅ API 테스트 성공!")
    print(f"📝 응답: {response.text}")
    print("\n🎉 모든 테스트를 통과했습니다! API를 사용할 준비가 되었습니다.")
    
except Exception as e:
    print(f"\n❌ API 테스트 실패: {str(e)}")
    print("\n💡 확인 사항:")
    print("1. API 키가 올바른지 확인하세요")
    print("2. 인터넷 연결을 확인하세요")
    print("3. Google AI Studio에서 API 키가 활성화되어 있는지 확인하세요")
    sys.exit(1)