from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from tools.file_tools import read_file, create_file, write_file, delete_file, list_files
from tools.rag_tools import add_document, search_document
from tools.search_tools import search_web
from langchain_core.messages import SystemMessage
from langgraph.checkpoint.memory import MemorySaver

#모델 생성
model = init_chat_model(
    "llama3.1:8b-instruct-q8_0",           #LLM 모델지정
    model_provider="ollama", # 로컬 실행 (Ollama)
    temperature=0.2,         # 창의성 조절 (0.0~2.0, 낮을수록 일관된 답변)
    keep_alive=120            # 메모리유지(VRAM 사용)
)

# 시스템 프롬포트
system_prompt = SystemMessage(content="""
1. 당신은 AI 에이전트 입니다.
2. 반드시 한국어로 답변하세요.
3. Tool을 사용할 때 JSON 형식으로 출력하지 말고 직접 실행하세요.
4. Tool 실행 결과를 자연스러운 문장으로 전달하세요
5. 절때 진실이 아닌 정보는 출력하지 않습니다
6. Tool 실행 후 결과만 간단히 말하세요. 코드 예시나 설명은 절대 하지 마세요.
7. "실제로 실행되지 않습니다" 같은 말은 절대 하지 마세요.
8. 사용자가 명확하게 파일 작업을 요청할 때만 Tool을 사용하세요.
9. 일반 대화, 인사, 질문에는 절대 Tool을 사용하지 마세요.
10. 파일 경로는 사용자가 말한 그대로 사용하세요.
11. 파일 경로가 불확실하면 사용자에게 묻지 말고 list_files Tool을 스스로 실행해서 확인하세요.
12. 파일 작업 전에 항상 list_files Tool로 먼저 파일 목록을 확인하고 정확한 경로를 찾으세요.
13. 벡터DB에 저장된 내용에 관한 질문은 절대 기억에 의존하지 말고 search_document tool을 실행하세요.
 """)

# Tool 목록
tools = [
    read_file,
    create_file, 
    write_file, 
    delete_file,
    list_files,
    search_web, 
    add_document, 
    search_document
    ]


#메모리 생성
memory = MemorySaver()

#에이전트 만들기
agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=system_prompt,
    checkpointer=memory,
)



# Ai 실행
while True:
    user_input = input("\n당신: ")
    
    if user_input == "종료":
        print("종료합니다.")
        break
    
    result = agent.invoke(
        {"messages": [("user", user_input)]},
        config={"configurable":{"thread_id": "1"}}
    )
    
    print(f"AI: {result['messages'][-1].content}")