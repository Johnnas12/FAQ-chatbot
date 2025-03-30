from hyperon import MeTTa
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
# Initialize MeTTa engine
engine = MeTTa()

# Define knowledge base in MeTTa format
knowledge_base = """
(FAQ "What is AI?" "AI stands for Artificial Intelligence, which simulates human intelligence in machines.")
(FAQ "What is ML?" "Machine Learning (ML) is a subset of AI that allows systems to learn from data.")
"""
# Load knowledge into MeTTa
engine.run(knowledge_base)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Set it in the environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini Model
gemini_model = genai.GenerativeModel("gemini-1.5-pro-002")

def query_knowledge_graph(question: str) -> str:
    query_result = engine.run(f'!(match &self (FAQ "{question}" $answer) $answer)')

    if query_result:
        result = str(query_result[0]).strip('[]"')
        print(f"Processed result: {repr(result)}")  
        if result and result.strip(): 
            return result
        return generate_rag_response(question)

    
def update_knowledge(question: str, answer: str):
    new_faq = f'(FAQ "{question}" "{answer}")'
    engine.run(new_faq)  

def generate_rag_response(question: str) -> str:
    """Use Gemini to generate an answer when the knowledge graph has no answer."""
    response = gemini_model.generate_content(question)
    return response.text if response.text else "I couldn't find an answer."
