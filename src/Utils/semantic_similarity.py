from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

similarity_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def semantic_similarity(phrase1, phrase2):

    embeddings = similarity_model.encode([phrase1, phrase2])

    first = embeddings[0].reshape(1, -1)
    second = embeddings[1].reshape(1, -1)

    return(cosine_similarity(first, second))