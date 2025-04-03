import numpy as np
import openai

openai.api_key = ""


def get_query_embedding(query):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=query
    )
    return np.array(response['data'][0]['embedding'])


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))