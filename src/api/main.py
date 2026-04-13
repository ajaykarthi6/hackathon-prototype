from fastapi import FastAPI

from src.api.schemas import QueryRequest, QueryResponse
from src.agent.logic import build_response

app = FastAPI(title="Interstellar Agent ADK")


@app.post("/query", response_model=QueryResponse)
def query_agent(payload: QueryRequest) -> QueryResponse:
    result = build_response(payload.prompt)
    return {"status": "success", "data": result}
