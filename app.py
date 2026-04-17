from core.orchestrator import run_system
from core.vectorstore import create_vectorstore

# create vector DB once
create_vectorstore()

query = input("Ask something: ")

result = run_system(query)

print("\n====================\n")
print(result)