"""Single source of truth for configuration.

Import values from here instead of calling os.getenv() throughout the project.

The .env file is loaded by its EXPLICIT path, so this works no matter which
directory you launch Python from (project root, Lecture01, or PyCharm console).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# src/config.py -> parents[1] = sentiment-classifier/ (the project root)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(ENV_PATH)  # copies .env values into os.environ


def _int(name: str, default: int) -> int:
    raw = os.getenv(name)
    return int(raw) if raw not in (None, "") else default


MODEL_NAME = os.getenv("MODEL_NAME", "bert-base-uncased")
MODEL_CACHE_DIR = os.getenv(
    "MODEL_CACHE_DIR", str(PROJECT_ROOT / "models" / "huggingface")
)
MAX_SEQUENCE_LENGTH = _int("MAX_SEQUENCE_LENGTH", 128)

BATCH_SIZE = _int("BATCH_SIZE", 16)
LEARNING_RATE = float(os.getenv("LEARNING_RATE", "0.00002"))
NUM_EPOCHS = _int("NUM_EPOCHS", 3)
DEVICE = os.getenv("DEVICE", "cpu")

DATA_DIR = PROJECT_ROOT / os.getenv("DATA_DIR", "data")
TRAIN_FILE = os.getenv("TRAIN_FILE", "train.csv")
VAL_FILE = os.getenv("VAL_FILE", "val.csv")
TEST_FILE = os.getenv("TEST_FILE", "test.csv")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "training.log")

WANDB_API_KEY = os.getenv("WANDB_API_KEY", "")
WANDB_PROJECT = os.getenv("WANDB_PROJECT", "sentiment-classifier")
WANDB_ENTITY = os.getenv("WANDB_ENTITY", "")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = _int("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "ml_experiments")
DB_USER = os.getenv("DB_USER", "mluser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


if __name__ == "__main__":
    print(f"Model: {MODEL_NAME}")
    print(f"Batch Size: {BATCH_SIZE}")
    print(f"Device: {DEVICE}")
    print(f"Batch size as integer: {BATCH_SIZE}")
    print(f"Data dir: {DATA_DIR}")
