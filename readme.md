# Indian History Agent

This project is a simple AI agent built using Google ADK that focuses only on Indian history topics.  
The main idea behind this project was to create a domain-specific assistant that can answer educational and historical questions instead of acting like a general-purpose chatbot.

The agent responds to topics related to:

- Ancient India
- Medieval India
- Modern India
- Indian Freedom Struggle
- Dynasties and Empires
- Historical Personalities
- Historical Events and Movements
- Indian Culture and Civilization

The agent is intentionally restricted to Indian history-related conversations.  
If a user asks something outside this domain, the agent politely refuses to answer.

---

# Tech Stack

- Python 3.11
- Google ADK
- Gemini Model
- FastAPI (via ADK runtime)

---

# Project Structure

```bash
GOOGLEADK/
│
├── Basic_agent/
│   ├── __init__.py
│   └── agent.py
│
├── .env
├── .gitignore
├── requirements.txt
└── .venv/