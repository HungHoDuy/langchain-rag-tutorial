from langchain.vectorstores import Chroma

# Assuming you have a connection to your Chroma database
chroma_path = 'chroma'
chroma_db = Chroma(persist_directory=chroma_path)

# Get the total number of documents
# 'Chroma' from langchain doesn't have a 'count' method, but you can use 'collection' attribute if accessible.
num_chunks = chroma_db._collection.count()
print(f"Total number of chunks in Chroma vector database: {num_chunks}")
