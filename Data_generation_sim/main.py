from src.dataset_generator import generate_dataset
from src.train_models import train_and_evaluate

def main():

    print("Generating dataset...")
    df = generate_dataset(1000)

    print("Training models...")
    results = train_and_evaluate(df)

    print("\nModel Comparison:")
    print(results)

if __name__ == "__main__":
    main()
