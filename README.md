Sha-Chatbot - *AI BOOK ASSISTANT*

Sha-Chatbot is a *full-stack AI chatbot* that answers user's natural language questions about books using a dataset.  
It intelligently interprets queries, retrieves book information from a CSV file, and responds with human-like answers powered by Google Gemini. The frontend UI is built with React, and the backend uses FastAPI.


FEATURES:
AI-Driven Understanding:
- Uses *Gemini LLM* to understand user intent (general vs book queries).
- Parses queries like:
  - *Top 5 books by rating*
  - *Books by Agatha Christie*
  - *Recommend books for me*
  - General conversation (“hi”, “I am bored”)

Smart Search Engine:
- Retrieves relevant book data from a CSV.
- Supports filters: title, author, category, ratings, sorting and limits.
- Handles invalid or ambiguous inputs gracefully.

Full Stack Architecture:
- **Frontend (React):** Clean chatbot UI + JSON debug tab.
- **Backend (FastAPI):** Handles API logic, classification, search, and parses dataset.
- **LLM Integration:** Gemini for natural language interpretation and replies.


PROJECT STRUCTURE:
Sha-Chatbot/
│
├── app/
│   ├── main.py
│   ├── gemini_handler.py
│   ├── csv_search.py
│   └── response_builder.py
│
├── book-chatbot-ui/
│   ├── public/
│   └── src/
│
├── data/
│   └── books.csv
│
├── requirements.txt
├── docker-compose.yml
└── README.md


HOW IT WORKS (FLOW):
User → React UI → FastAPI API → Gemini LLM → CSV Search → Gemini Response → UI Display

SETUP & INSTALLATION:
Prerequisites
- Python 3.9+
- Node.js

BACKEND SETUP:

1. Clone repository
git clone https://github.com/M-SHALINI2005/Sha-Chatbot.git
cd Sha-Chatbot

2. Create virtual environment
python -m venv venv

Activate
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
GEMINI_API_KEY=YOUR_API_KEY

5. Run server
uvicorn app.main:app --reload

API Docs:
http://127.0.0.1:8000/doc

FRONTEND SETUP:

cd book-chatbot-ui
npm install
npm start

Frontend runs at:
http://localhost:3000
