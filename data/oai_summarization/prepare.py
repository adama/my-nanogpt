import os
import tiktoken
import numpy as np
import re
import json

# encodes some data for SFT
# TODO: how much and should it be disjoint from {PM, PPO} datasets?

datadir = os.path.join(os.path.dirname(__file__), "comparisons")

all_samples = []
for fname in os.listdir(datadir):
    try:
        batchno = int(re.search("batch(\d+)", fname).group(1))
        if batchno % 3 == 0:
            with open(os.path.join(datadir, fname), "r", encoding="utf-8") as f:
                # TODO orjson
                for line in f:
                    obj = json.loads(line)
                    summary = obj["summaries"][0]["text"] if obj["summaries"][0]["policy"] == "ref" else obj["summaries"][1]["text"] 
                    all_samples.append(dict(
                        article=obj["info"]["article"],
                        summary=summary
                    ))
    except:
        continue

np.random.seed(2024)
train_ixs = np.random.choice(range(len(all_samples)), int(0.9*len(all_samples)), replace=False)
val_ixs = [ix for ix in range(len(all_samples)) if ix not in set(train_ixs)]

def stringify_datum(ix):
    return f"<|article|> {all_samples[ix]['article']} <|summary|> {all_samples[ix]['summary']}"

train_data = "\n".join([stringify_datum(ix) for ix in train_ixs])
val_data = "\n".join([stringify_datum(ix) for ix in val_ixs])

enc = tiktoken.get_encoding("gpt2")

train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train has 381,946 tokens
# val has 45,262 tokens