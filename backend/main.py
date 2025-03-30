from fastapi import FastAPI
from knowledge_graph import query_knowledge_graph, update_knowledge
from pydantic import BaseModel


app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class KnowledgeUpdate(BaseModel):
    question: str
    answer: str

@app.get("/")
async def root():
    return {"message": "Welcome to domain specific chatbot Knowledge Graph API!🚀"}

@app.post("/chat")
async def chat(request: QuestionRequest):
    response = query_knowledge_graph(request.question)
    if not response:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"response": response}

@app.post("/update_knowledge")
async def update_knowledge_endpoint(data: KnowledgeUpdate):
    update_knowledge(data.question, data.answer)
    return {"message": "Knowledge updated successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
