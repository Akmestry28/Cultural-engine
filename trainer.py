import argparse
from models.model_trainer import ModelTrainer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_file", type=str, default="data/training_data.json")
    parser.add_argument("--epochs", type=int, default=3)
    args = parser.parse_args()

    trainer = ModelTrainer(args.train_file)
    trainer.train(epochs=args.epochs)
    print("Training complete! Model saved.")
