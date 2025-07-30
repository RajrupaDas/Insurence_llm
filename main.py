from fastapi import FastAPI
from pydantic import BaseModel
from search_clause import search
from llm_decision import ask_llm
import uvicorn

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/query")
def process_query(input_data: QueryInput):
    query = input_data.query
    clause, score = search(query)[0]
    llm_response = ask_llm(clause, query)

    return {
        "input_query": query,
        "matched_clause": clause,
        "decision_result": llm_response
    }

@app.get("/")
def root():
    return {"message": "ClauseWise API is running"}

# Optional: for local run
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

