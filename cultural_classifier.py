from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from config import BASE_MODEL, CULTURAL_CATEGORIES

class FreeCulturalClassifier:
    def __init__(self):
        self.model = SentenceTransformer(BASE_MODEL)
        self.categories = CULTURAL_CATEGORIES
        self.category_embeddings = self.model.encode(self.categories, normalize_embeddings=True)
    
    def classify(self, text):
        text_emb = self.model.encode([text], normalize_embeddings=True)
        similarities = cosine_similarity(text_emb, self.category_embeddings)
        idx = np.argmax(similarities)
        return {"category": self.categories[idx], "score": float(similarities[0][idx])}

class OptimizedCulturalEngine:
    def __init__(self):
        self.classifier = FreeCulturalClassifier()
    
    def analyze_cultural_context(self, text, user_metadata=None):
        result = self.classifier.classify(text)
        result.update({
            "user_metadata": user_metadata,
            "suggestions": [f"Explore {result['category']} practices"]
        })
        return result