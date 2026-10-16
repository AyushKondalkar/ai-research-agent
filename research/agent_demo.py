
import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

# Load API keys from .env
load_dotenv()

# Check the Tavily API key
if not os.getenv("TAVILY_API_KEY"):
    raise ValueError("TAVILY_API_KEY is missing from .env")

# Create the search tool
search_tool = TavilySearch(max_results=2)

# Execute a search
result = search_tool.invoke({
    "query": "What is the capital of India in 2026?"
})

# Display search results
print(result)
