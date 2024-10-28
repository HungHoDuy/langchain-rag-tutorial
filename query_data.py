from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma

CHROMA_PATH = "chroma"

class CustomEmbeddingFunction:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed_query(self, text):
        return self.model.encode(text, convert_to_tensor=True).tolist()  # Convert to list for compatibility

    def embed_documents(self, texts):
        return self.model.encode(texts, convert_to_tensor=True).tolist()  # Convert to list for compatibility

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = CustomEmbeddingFunction('sentence-transformers/all-mpnet-base-v2')
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    # Prepare context text with source information from results
    context_text = "\n\n---\n\n".join(
        [f"Source: {doc.metadata.get('source', 'Unknown')}\nContent: {doc.page_content}" for doc, _score in results]
    )

    # Output the context text with source information
    print(f"Context for the query: {context_text}")

if __name__ == "__main__":
    query = "What to eat in Quy Nhon"
    query_rag(query)
