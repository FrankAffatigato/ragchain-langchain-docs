import os
from pinecone import Pinecone

# Initialize Pinecone client
api_key = "api_key"  # Replace with your actual API key
pc = Pinecone(api_key=api_key)

# Define your index name
index_name = "langchain-doc-index"

# Access the index
index = pc.Index(index_name)

# Get index stats
stats = index.describe_index_stats()
print(f"Number of records: {stats['total_vector_count']}")