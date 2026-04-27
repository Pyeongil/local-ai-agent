from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from langchain.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
import os

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    collection_name="documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)

@tool
def add_document(filepath: str) -> str:
    """파일을 읽어 벡터DB에 저장합니다. 텍스트 파일, pdf 파일을 지원합니다."""
    if not os.path.exists(filepath):
        return f"{filepath} 파일이 존재하지 않습니다."
    
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(filepath)
    elif ext in [".txt", ".py", ".md", ".js", ".html"]:
        loader = TextLoader(filepath, encoding="utf-8")
    else:
        return f"{ext} 형식은 지원하지 않습니다."
    
    docs = loader.load()
    chunks = splitter.split_documents(docs)
    vectorstore.add_documents(chunks)
    return f"{filepath} 총 {len(chunks)}개 청크로 저장되었습니다."

@tool
def search_document(query: str) -> str:
    """벡터DB에서 질문과 관련된 문서 내용을 검색합니다."""
    results = vectorstore.similarity_search(query, k=3)
    if not results:
        return "관련 문서를 찾을 수 없습니다."
    return "\n\n".join(
        f"[{i+1}]\n{doc.page_content}" for i, doc in enumerate(results)
    )
