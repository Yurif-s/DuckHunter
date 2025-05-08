from duckduckgo_search import DDGS

def search_news(query, max_results=10):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results)
        response = []
        for result in results:
            response.append({
                "title": result.get("title"),
                "body": result.get("body"),
                "href": result.get("href")
            })
    return response