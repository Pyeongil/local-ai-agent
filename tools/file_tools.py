from langchain.tools import tool
import os

#파일 읽기 Tool
@tool
def read_file(filepath: str) -> str:                 # 어떤파일을 읽을지 경로를 받음
    """파일 내용을 읽어서 반환합니다"""                # 단순주석이 아닌 Ai가 읽는 설명
    with open(filepath, 'r', encoding='utf-8') as f: # 파일을 열고 작업이 끝나면 자동으로 닫아줌
        return f.read()
    
#파일 생성 및 덮어쓰기
@tool
def write_file(filepath: str, content: str) -> str:
    """파일을 생성하거나 내용을 수정할때 사용합니다."""
    if os.path.exists(filepath):                         # 경로에 파일이 있으면 수정 및 저장
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"{filepath} 수정 및 저장 완료"            # AI에게 주입
    else:
        with open(filepath, 'w', encoding='utf-8') as f: # 경로에 파일이 없으면 생성 및 저장
            f.write(content)
        return f"{filepath} 생성 및 저장 완료"            # AI에게 주입
    
