from knowledge_graph import query_knowledge_graph

def get_response():
    response = query_knowledge_graph('"What is AI?"')
    return response if response else "I don't know the answer yet."
