from core.vectorstore import search_vectorstore

def research_agent(query):
    context = search_vectorstore(query)
    return context