
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import uuid

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Article(BaseModel):
    email: str
    article_url: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/process-article/")
async def process_article(article: Article):
    session_id = str(uuid.uuid4())
    n8n_webhook_url = "https://shamsul-islam-2202.app.n8n.cloud/webhook/webhook"  # Replace with your n8n webhook URL

    payload = {
        "email": article.email,
        "article_url": article.article_url,
        "session_id": session_id,
    }
    print(f"Payload being sent to n8n: {payload}")

    try:
        print(f"Attempting to send data to n8n webhook: {n8n_webhook_url}")
        response = requests.post(n8n_webhook_url, json=payload)
        print(f"n8n response Status Code: {response.status_code}")
        print(f"n8n response Body: {response.text}")
        response.raise_for_status()  # Raise an exception for bad status codes
        return {"message": "Article processing started successfully."}
    except requests.exceptions.RequestException as e:
        print(f"Error calling n8n webhook: {e}")
        return {"message": f"Failed to trigger n8n workflow: {e}"}

