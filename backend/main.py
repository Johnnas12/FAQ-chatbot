from fastapi import FastAPI
from knowledge_graph import query_knowledge_graph

app = FastAPI()

@app.get("/chat")
def chat(question: str):
    response = query_knowledge_graph(question)
    return {"response": response}  # JSON serializable output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
