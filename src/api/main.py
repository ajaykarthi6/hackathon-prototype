from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.api.schemas import QueryRequest, QueryResponse
from src.agent.logic import build_response

app = FastAPI(title="Interstellar Agent ADK")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/query", response_model=QueryResponse)
def query_agent_api(payload: QueryRequest) -> QueryResponse:
    result = build_response(payload.prompt)
    return {"status": "success", "data": result}


@app.post("/web-query", response_class=HTMLResponse)
async def query_agent_web(request: Request, prompt: str = Form(...)):
    result = build_response(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "response": result})


