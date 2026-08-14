import os

from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()

API_KEY = os.getenv("TAVILY_API_KEY")

if not API_KEY:
    raise ValueError(
        "TAVILY_API_KEY is missing from .env"
    )


client = TavilyClient(api_key=API_KEY)


def search_web(query, max_results=5):
    """
    Search the live web for evidence related to a claim.

    Args:
        query: Search query string.
        max_results: Maximum number of sources to return.

    Returns:
        List of search result dictionaries.
    """

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=max_results
    )

    results = []

    for result in response.get("results", []):
        results.append({
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "content": result.get("content", ""),
            "score": result.get("score", 0)
        })

    return results