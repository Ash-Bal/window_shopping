from pathlib import Path
from tqdm import tqdm

import torch
import pandas as pd
import numpy as np
import requests
from PIL import Image
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer
from marketplace_assistant.config import RAW_IMAGE_FILE_DIR, PROCESSED_DATA_DIR


def main():
    model_id = "vikhyatk/moondream2"
    if torch.cuda.is_available():
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("mps")
    elif torch.backends.mps.is_available():
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to("mps")
    else:
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    marketplace_data_path = PROCESSED_DATA_DIR / "marketplace_data.csv"
    marketplace_data = pd.read_csv(
        marketplace_data_path,
    )

    batch_size = 2
    batch_sample = marketplace_data.sample(4)
    data_len = len(batch_sample)

    ans = []

    for chunk in tqdm(np.array_split(batch_sample, data_len / batch_size)):
        chunk["full_path"] = str(RAW_IMAGE_FILE_DIR) + "/" + chunk["path"].astype(str)
        chunk_imgs = chunk["full_path"].tolist()
        chunk_imgs = [Image.open(name) for name in chunk_imgs]
        prompt = [
            "Write a caption that describes the object in the image in a concise manner."
        ] * len(chunk)
        ans = ans + model.batch_answer(images=chunk_imgs, prompts=prompt, tokenizer=tokenizer)

    batch_sample["ai_desc"] = ans

    batch_sample.to_csv(PROCESSED_DATA_DIR / "marketplace_data_captioned_images.csv", index=False)


if __name__ == "__main__":
    main()
