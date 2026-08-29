from datasets import load_dataset
from pathlib import Path

dataset = load_dataset("dgslibisey/MuSiQue")

train = dataset["train"]
# test = dataset["test"]

output_dir = Path("data/MuSiQue/clean")
output_dir.mkdir(parents=True, exist_ok=True)

train_file = output_dir / "train.json"
# test_file = output_dir / "test.csv"

train.to_json(train_file)

# train.to_csv(train_file)
# test.to_csv(test_file)