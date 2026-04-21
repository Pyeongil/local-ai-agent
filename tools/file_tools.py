from langchain.tools import tool
import os

#파일 읽기 Tool
@tool
def read_file(filepath: str) -> str:                 # 어떤파일을 읽을지 경로를 받음
    """파일 내용을 읽어서 반환합니다"""                # 단순주석이 아닌 Ai가 읽는 설명
    with open(filepath, 'r', encoding='utf-8') as f: # 파일을 열고 작업이 끝나면 자동으로 닫아줌
        return f.read()
    
# 빈 파일 생성
@tool
def create_file(filepath: str) -> str:
    """빈 파일을 생성할때 사용합니다."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("")
    return f"{filepath} 파일 생성완료"

# 파일 내용 수정 및 덮어쓰기
@tool
def write_file(filepath: str, content: str) -> str:
    """파일에 내용을 작성하거나 수정할때 사용합니다. 파일이 없으면 생성 후 내용을 저장합니다."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"{filepath} 수정 및 덮어쓰기 완료"

# 파일 삭제 
@tool
def delete_file(filepath: str) -> str:
    """파일을 삭제할때 사용합니다"""
    if os.path.exists(filepath):                       # 파일 있는지 확인
        os.remove(filepath)                            # 경로에 파일이있으면 삭제
        return f"{filepath} 파일 삭제 완료"             # Ai에게 주입
    else:
        return f"{filepath} 파일이 존재하지 않습니다."  # 파일이 없으면 반환