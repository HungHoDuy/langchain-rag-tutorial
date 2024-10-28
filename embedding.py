from transformers import AutoTokenizer, AutoModel
import torch

# Load the pre-trained model and tokenizer
model_name = "sentence-transformers/all-mpnet-base-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embeddings(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # Get the model's output
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Mean pooling to get sentence embeddings
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

if __name__ == "__main__":
    sample_text = "This is a test sentence for generating embeddings."
    embedding_vector = get_embeddings(sample_text)
    print("Generated Embedding:")
    print(embedding_vector)
