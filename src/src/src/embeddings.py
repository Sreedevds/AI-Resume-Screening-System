from sentence_transformers import SentenceTransformer
import numpy as np


# ---------------------------------------------------------
# LOAD TRANSFORMER MODEL
# ---------------------------------------------------------

_model = None


def load_embedding_model():
    """
    Load the Sentence Transformer model.

    The model is loaded only once and reused for
    subsequent embedding operations.
    """

    global _model

    if _model is None:
        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model


# ---------------------------------------------------------
# GENERATE SINGLE EMBEDDING
# ---------------------------------------------------------

def generate_embedding(text):
    """
    Convert text into a semantic embedding vector.
    """

    model = load_embedding_model()

    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding


# ---------------------------------------------------------
# GENERATE MULTIPLE EMBEDDINGS
# ---------------------------------------------------------

def generate_embeddings(texts):
    """
    Generate embeddings for multiple documents.
    """

    model = load_embedding_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    return embeddings


# ---------------------------------------------------------
# NORMALIZE EMBEDDING
# ---------------------------------------------------------

def normalize_embedding(embedding):
    """
    Normalize an embedding vector.
    """

    norm = np.linalg.norm(
        embedding
    )

    if norm == 0:
        return embedding

    return embedding / norm
