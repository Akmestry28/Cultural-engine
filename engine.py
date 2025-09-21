from models.cultural_classifier import OptimizedCulturalEngine

if __name__ == "__main__":
    engine = OptimizedCulturalEngine()
    text = input("Enter cultural text: ")
    result = engine.analyze_cultural_context(text, {"user_id": "test", "region": "Maharashtra"})
    print(result)
