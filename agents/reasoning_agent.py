def reasoning_agent(query, context):
    if "No relevant data" in context:
        return "I couldn't find information to answer that."
    
    # Simulating 'reasoning' by summarizing the context
    return f"Based on the research: {context}"