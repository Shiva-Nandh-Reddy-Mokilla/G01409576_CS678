# google_search.py
import requests
from gentopia.tools.basetool import BaseTool

class GoogleSearchTool(BaseTool):
    name = "google_search"
    description = ("Perform a Google search and return relevant search results.")
    
    def _run(self, query: str, num_results: int = 5) -> str:
        search_url = f"https://www.google.com/search?q={query}&num={num_results}"
        response = requests.get(search_url)
        results = response.text  # Extract search results from the HTML response
        return results

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
