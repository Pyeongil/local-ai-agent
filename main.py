from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from tools.file_tools import read_file, create_file, write_file, delete_file

#모델 생성
model = init_chat_model(
    "qwen2.5:14b",           #LLM 모델지정
    model_provider="ollama", # 로컬 실행 (Ollama)
    temperature=0.2,         # 창의성 조절 (0.0~2.0, 낮을수록 일관된 답변)
    keep_alive=120            # 메모리유지(VRAM 사용)
)

# Tool 목록
tools = [read_file, create_file, write_file, delete_file]

#에이전트 만들기
agent = create_react_agent(
    model=model, # 모델 지정 qwen2.5:14b
    tools=tools  # tool 지정
)

# Ai 실행
while True:
    user_input = input("\n당신: ")
    
    if user_input == "종료":
        print("종료합니다.")
        break
    
    result = agent.invoke({
        "messages": [("user", user_input)]
    })
    
    print(f"AI: {result['messages'][-1].content}")