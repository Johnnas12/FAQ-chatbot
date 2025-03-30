from fastapi import FastAPI, HTTPException
from knowledge_graph import query_knowledge_graph, update_knowledge
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Pydantic models for request bodies
class QuestionRequest(BaseModel):
    question: str

class KnowledgeUpdate(BaseModel):
    question: str
    answer: str

# Configure Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Set it in the environment variables.")
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-pro-002")

@app.post("/chat")
async def chat(request: QuestionRequest):
    """Endpoint to query the knowledge graph for an answer."""
    response = query_knowledge_graph(request.question)
    if not response:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"response": response}

@app.post("/update_knowledge")
async def update_knowledge_endpoint(data: KnowledgeUpdate):
    """Endpoint to update knowledge in the knowledge graph."""
    update_knowledge(data.question, data.answer)
    return {"message": "Knowledge updated successfully!"}

# Run the FastAPI app using Uvicorn (only for local dev)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
