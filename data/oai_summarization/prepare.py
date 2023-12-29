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

print(len(all_samples))