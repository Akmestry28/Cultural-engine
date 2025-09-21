from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models" / "saved"
USER_DATA_DIR = DATA_DIR / "user_data"

for dir_path in [DATA_DIR, MODELS_DIR, USER_DATA_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

BASE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
MAX_LENGTH = 128
BATCH_SIZE = 32
LEARNING_RATE = 2e-5

CULTURAL_CATEGORIES = [
    "Family_Nuclear", "Family_Extended", "Family_Marriage", "Family_Children",
    "Religious_Hindu", "Religious_Muslim", "Religious_Sikh", "Religious_Christian",
    "Regional_Maharashtra", "Regional_Tamil", "Regional_Bengali", "Regional_Punjab",
    "Festival_Major", "Festival_Regional", "Festival_Personal", "Festival_Seasonal",
    "Food_Traditional", "Food_Regional", "Food_Street", "Food_Homemade",
    "Daily_Greeting", "Daily_Work", "Daily_School", "Daily_Shopping",
    "Music_Classical", "Music_Folk", "Music_Modern", "Music_Devotional",
    "Language_Hindi", "Language_Regional", "Language_English", "Language_Mixed",
    "Social_Respect", "Social_Hierarchy", "Social_Community", "Social_Individual",
    "Tradition_Wedding", "Tradition_Birth", "Tradition_Death", "Tradition_Coming_of_Age",
    "Emotion_Joy", "Emotion_Sadness", "Emotion_Anger", "Emotion_Love",
    "Business_Trade", "Education_Learning", "Health_Wellness", "Sports_Games",
    "Art_Painting", "Craft_Making"
]
