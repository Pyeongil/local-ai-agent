1.LangChain과 LangGraph를 활용한 로컬 환경 기반 AI 에이전트 개인 프로젝트

프로젝트 소개

AI 에이전트를 직접 만들어보면서 구조를 이해하고
활용 능력을 키우기 위해 시작한 개인 프로젝트입니다.

2.목표 기능
- [ ] 파일 생성, 수정, 삭제
- [ ] 웹 검색으로 최신 정보 수집
- [ ] 문서 내용 검색 (RAG)
- [ ] 코드 자동 생성 및 실행

3.기술 스택
| 기술 | 용도 |
|------|------|
| Python | 메인 언어 |
| LangChain | Tool 제작 |
| LangGraph | 에이전트 구성 |
| Ollama | 로컬 LLM 실행 |
| Tavily API | 웹 검색 |
| ChromaDB | 벡터 DB (RAG) |

4.프로젝트 구조(추가하면서 진행 예정)
```
local-ai-agent/
├── tools/
│   ├── __init__.py
│   ├── file_tools.py
│   └── search_tools.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```
벨로그 주소
https://velog.io/@qkek8823/posts

ㅡㅡㅡ개발 일지ㅡㅡㅡ
| 날짜       | 내용 |
|----------- |------|
| 2026.04.21 | 프로젝트 기획 및 환경 세팅, 파일읽기 Tool 구현 | 
| 2026.04.22 | 에이전트 Tool 작업 및 LangGraph 연결 및 테스트 진행 | 
