import torch
from torch.utils.data import Dataset, DataLoader
from sentence_transformers import SentenceTransformer, losses, InputExample
import json
from config import BASE_MODEL, BATCH_SIZE, LEARNING_RATE, MAX_LENGTH

class CulturalDataset(Dataset):
    def __init__(self, data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

class ModelTrainer:
    def __init__(self, train_file, model_path="models/saved/cultural_model"):
        self.dataset = CulturalDataset(train_file)
        self.model = SentenceTransformer(BASE_MODEL)
        self.model_path = model_path

    def train(self, epochs=3):
        examples = [InputExample(texts=[item['text']], label=float(item['label'])) for item in self.dataset]
        train_dataloader = DataLoader(examples, shuffle=True, batch_size=BATCH_SIZE)
        train_loss = losses.CosineSimilarityLoss(self.model)
        self.model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=epochs, warmup_steps=100)
        self.model.save(self.model_path)
