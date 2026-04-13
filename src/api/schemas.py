from typing import Any

from pydantic import BaseModel


class QueryRequest(BaseModel):
    prompt: str


class QueryResponse(BaseModel):
    status: str
    data: dict[str, Any]
