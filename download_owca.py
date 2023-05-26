import os
import json
from datasets import load_dataset

dataset = load_dataset("emplocity/owca")
download = []
for d in dataset["train"]:
    download.append(d)

data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

with open(os.path.join(data_dir, "owca.json"), "w", encoding="utf-8") as file:
    json.dump(download, file, indent=4, ensure_ascii=False)
