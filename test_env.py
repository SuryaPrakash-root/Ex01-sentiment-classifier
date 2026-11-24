# test_env.py
import os
from pathlib import Path
from dotenv import load_dotenv

# TODO: Load .env file
ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_PATH)

# TODO: Read and print environment variables
model_name = os.getenv("MODEL_NAME")
batch_size = os.getenv("BATCH_SIZE")
device = os.getenv("DEVICE")

print(f"Model: {model_name}")
print(f"Batch Size: {batch_size}")
print(f"Device: {device}")

# TODO: Handle missing variables
for name, value in {
    "Model": model_name,
    "Batch_size": batch_size,
    "Device": device,
}.items():
    if not value:
        print(f"Warning: {name} missing in .env file")
        continue
db_password = os.getenv("DB_PASSWORD")
if not db_password:
    print("Warning: DB_PASSWORD missing in .env file")
elif db_password in ("changeme", "postgres", "password"):
    print("WARNING: Using default database password. Change in production!")

# TODO: Type conversion
batch_size_int = int(os.getenv("BATCH_SIZE", "32"))
print(f"Batch size as integer: {batch_size_int}")