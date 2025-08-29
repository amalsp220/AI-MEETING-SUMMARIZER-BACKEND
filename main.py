from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow frontend (GitHub Pages) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your GitHub Pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1"

@app.post("/summarize")
async def summarize(request: Request):
    body = await request.json()
    transcript = body.get("transcript", "")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "Summarize this meeting:"},
            {"role": "user", "content": transcript}
        ]
    }

    response = requests.post(f"{GROQ_API_URL}/chat/completions", headers=headers, json=payload)
    return response.json()
