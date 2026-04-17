import sys
import os

# This line allows the 'core' folder to "see" the 'agents' folder next to it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.research_agent import research_agent
from agents.reasoning_agent import reasoning_agent
from agents.decision_agent import decision_agent

def run_system(query):
    context = research_agent(query)
    reasoning = reasoning_agent(query, context)
    final = decision_agent(reasoning)
    return final