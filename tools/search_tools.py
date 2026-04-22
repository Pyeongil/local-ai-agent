from langchain.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_web(query: str) -> str:
    """인터넷에서 정보를 검색할때 사용합니다."""
    response = client.search(query=query, max_results=3)
    results = response.get("results", [])
    if not results:
        return "검색 결과가 없습니다."
    return "\n\n".join(
        f"제목: {r['title']}\nURL: {r['url']}\n내용: {r['content']}" for r in results
    )
