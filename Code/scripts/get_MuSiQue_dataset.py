from datasets import load_dataset
from pathlib import Path

dataset = load_dataset("dgslibisey/MuSiQue")

train = dataset["train"]
validation = dataset["validation"]

output_dir = Path("data/MuSiQue/clean")
output_dir.mkdir(parents=True, exist_ok=True)

train_file = output_dir / "train.json"
validation_file = output_dir / "validation.json"


train.to_json(train_file)
validation.to_json(validation_file)
