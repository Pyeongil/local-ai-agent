from langchain.chat_models import init_chat_model
from tools.file_tools import read_file

#모델 생성
model = init_chat_model(
    "qwen2.5:14b",           #LLM 모델지정
    model_provider="ollama", # 로컬 실행 (Ollama)
    temperature=0.2,         # 창의성 조절 (0.0~2.0, 낮을수록 일관된 답변)
    keep_alive=120            # 메모리유지(VRAM 사용)
)

result = read_file.invoke({"filepath": "test.txt"})
print(result)