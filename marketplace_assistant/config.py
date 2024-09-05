from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
RAW_LISTINGS_DIR = RAW_DATA_DIR / "abo-listings" / "listings" / "metadata"
RAW_IMAGE_DIR = RAW_DATA_DIR / "abo-images-small" / "images"
RAW_IMAGE_METADATA_DIR = RAW_IMAGE_DIR / "metadata"
RAW_IMAGE_FILE_DIR = RAW_IMAGE_DIR / "small"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

GOOG_ROOT = Path("/content/drive/MyDrive/")
GOOG_RAW_DATA = GOOG_ROOT / "marketplace_data"
GOOG_RAW_IMAGE_FILE_DIR = GOOG_RAW_DATA / "raw" / "abo-images-small" / "images" / "small"
GOOG_PROCESSED_DATA_DIR = GOOG_RAW_DATA / "processed"

MODELS_DIR = PROJ_ROOT / "models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    pass
