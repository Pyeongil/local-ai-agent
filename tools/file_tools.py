from langchain.tools import tool
import os

#파일 읽기 Tool
@tool
def read_file(filepath: str) -> str:                 # 어떤파일을 읽을지 경로를 받음
    """파일 내용을 읽어서 반환합니다"""                # 단순주석이 아닌 Ai가 읽는 설명
    with open(filepath, 'r', encoding='utf-8') as f: # 파일을 열고 작업이 끝나면 자동으로 닫아줌
        return f.read()