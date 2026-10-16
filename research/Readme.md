# AI Research Agent

An AI-powered research assistant built with LangChain, Google Gemini, and Tavily Search. It can answer questions and search the web for current information when needed.

## Features

- Uses Google Gemini as the language model.
- Searches the web using Tavily.
- Uses a LangChain agent to decide when to use the search tool.
- Provides research answers with relevant source URLs.
- Supports interactive questions through the terminal.

## Tech Stack

- Python
- LangChain
- Google Gemini
- Tavily Search
- python-dotenv

## Project Structure

```text
Agent/
├── research/
│   └── research_agent.py
├── .env                 # Keep private; do not upload
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Agent
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholders with your own API keys. **Never share or upload your real API keys.**

### 5. Run the agent

```powershell
python research/research_agent.py
```

Type a research question to begin. Type `exit` to stop the agent.

## How It Works

The user submits a question. The LangChain agent uses Google Gemini to interpret the request and decides whether Tavily Search is needed. It then generates a response using the available information.

## Future Improvements

- Add conversation memory.
- Build a web interface using Streamlit or FastAPI.
- Add source validation and answer evaluation.
- Add logging and error handling.