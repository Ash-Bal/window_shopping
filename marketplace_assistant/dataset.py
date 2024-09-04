from pathlib import Path

from tqdm import tqdm

from marketplace_assistant.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path=RAW_DATA_DIR / "dataset.csv",
    output_path=PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    for i in tqdm(range(10), total=10):
        if i == 5:
            pass
    # -----------------------------------------


if __name__ == "__main__":
    main()
