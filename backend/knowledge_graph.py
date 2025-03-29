from hyperon import MeTTa
# Initialize MeTTa engine
engine = MeTTa()

# Define knowledge base
knowledge_base = """
(FAQ "What is AI?" "AI stands for Artificial Intelligence, which simulates human intelligence in machines.")
(FAQ "What is ML?" "Machine Learning (ML) is a subset of AI that allows systems to learn from data.")
"""
# Load knowledge into MeTTa
engine.run(knowledge_base)

def query_knowledge_graph(question: str) -> str:
    query_result = engine.run(f'!(match &self (FAQ "{question}" $answer) $answer)')

    if query_result:
        result = str(query_result[0]).strip('[]"')
        print(f"Processed result: {repr(result)}")  
        if result and result.strip(): 
            return result
        return"No answer found in knowledge graph."
