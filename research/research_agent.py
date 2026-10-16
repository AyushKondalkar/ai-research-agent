
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent

# Load API keys
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# Create the web search tool
search_tool = TavilySearch(max_results=3)

# Create the agent
agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt=(
        "You are a research assistant. "
        "Use Tavily to search for current information when needed. "
        "Provide clear answers based on the information available. "
        "When using search results, include relevant source URLs."
    ),
)

# Interactive conversation
while True:
    question = input("\nAsk your research agent (or type 'exit'): ").strip()

    if question.lower() == "exit":
        print("Research agent stopped.")
        break

    if not question:
        continue

    try:
        response = agent.invoke({
            "messages": [
                {"role": "user", "content": question}
            ]
        })

        print("\nAgent answer:\n")
        print(response["messages"][-1].content)

    except Exception as error:
        print(f"Error: {error}")
