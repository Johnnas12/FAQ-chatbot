from fastapi import FastAPI
from knowledge_graph import query_knowledge_graph
from pydantic import BaseModel



app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(request: QuestionRequest):
    response = query_knowledge_graph(request.question)
    if not response:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
