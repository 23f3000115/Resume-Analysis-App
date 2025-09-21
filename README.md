# Resume Analysis App

Resume Analysis App built with:
- Frontend: HTML / CSS / JavaScript
- Backend: Python + Flask
- AI: LangChain + (placeholder) Gemini integration (instructions included)

## Features included:
- PDF upload endpoint and simple parsing pipeline (PDF -> extracted text)
- Keyword & skill extraction (basic rule-based + spaCy ready)
- Resume scoring skeleton (clarity, impact, keywords, completeness)
- Section-wise suggestions and summary generator hooks (uses LangChain/Gemini)
- Job title skills gap analysis endpoint
- Interactive editor front-end (in-browser) with rewrite suggestions placeholder
- ATS preview generation endpoint
- Account scaffolding notes (no auth implemented by default)

## How to run (local)
1. Create and activate a virtualenv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Set environment variables (example):
   ```bash

   # For Gemini/LangChain usage, create a .env or export keys:
   export GEMINI_API_KEY="your_gemini_api_key_here"
   ```
3. Run the app:
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```
4. Open http://127.0.0.1:5000 in your browser.

## Gemini / LangChain Notes
- This scaffold includes `ai_services.py` with *placeholder* code showing how you would call an LLM through LangChain.
- Replace placeholders with your provider-specific client/credentials. The code comments provide guidance.

