from duckduckgo_search import DDGS
from services.extract_source import extract_source

def search_news(query: str, max_results=10) -> list:
    results = DDGS().text(query, max_results)
    response = []
    for result in results:
        response.append({
            "title": result.get("title"),
            "body": result.get("body"),
            "href": result.get("href"),
            "source": extract_source(result.get("href"))
        })
    return response