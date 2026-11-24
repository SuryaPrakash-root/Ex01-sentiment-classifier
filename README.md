# Sentiment Classifier

Fine-tune a BERT-based sentiment classifier (positive / negative) with a
reproducible, configuration-driven Python project.

> **Status:** environment setup, configuration, and tooling are complete and
> verified. The training pipeline (`src/train.py`, `src/evaluate.py`,
> `src/utils/`) is still scaffolding — see [Project Status](#project-status).

---

## Features

- **Reproducible environment** — pinned dependencies, one-command setup,
  Python 3.11 virtual environment.
- **Single source of truth for config** — every setting lives in `.env` and is
  read once by `src/config.py`. No scattered `os.getenv()` calls.
- **Secrets never committed** — `.env` is gitignored; `.env.example` documents
  every option.
- **Self-verifying setup** — `verify_setup.py` checks Python version, venv,
  dependencies, project layout, and Git configuration.
- **Optional experiment tracking** — Weights & Biases support (disabled when
  `WANDB_API_KEY` is blank).

---

## Requirements

| Tool  | Version |
|-------|---------|
| Python | 3.11+ |
| Git | 2.x |
| pip | latest |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/SuryaPrakash-root/Ex01-sentiment-classifier.git
cd Ex01-sentiment-classifier

# 2. Run the automated setup (creates venv, installs deps, bootstraps .env)
./setup.sh

# 3. Activate the environment
source venv/bin/activate

# 4. Verify everything works
python verify_setup.py
```

### Manual setup (if you prefer not to use `setup.sh`)

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
cp .env.example .env      # then edit .env with your real values
python verify_setup.py
```

---

## Configuration

All configuration is read from `.env` in the project root by
[`src/config.py`](src/config.py). Copy `.env.example` to `.env` and adjust.

### Model

| Variable | Default | Description |
|----------|---------|-------------|
| `MODEL_NAME` | `bert-base-uncased` | HuggingFace model id |
| `MODEL_CACHE_DIR` | `./models/huggingface` | Where weights are cached |
| `MAX_SEQUENCE_LENGTH` | `128` | Max tokens per example |

### Training

| Variable | Default | Description |
|----------|---------|-------------|
| `BATCH_SIZE` | `16` | Lower to `8` if you run out of memory |
| `LEARNING_RATE` | `0.00002` | Typical BERT fine-tuning LR (`2e-5`) |
| `NUM_EPOCHS` | `3` | Training epochs |
| `DEVICE` | `cpu` | `cpu`, `mps` (Apple Silicon), or `cuda` (NVIDIA) |

### Data

| Variable | Default | Description |
|----------|---------|-------------|
| `DATA_DIR` | `./data` | Folder holding the CSVs |
| `TRAIN_FILE` | `train.csv` | Training split |
| `VAL_FILE` | `val.csv` | Validation split |
| `TEST_FILE` | `test.csv` | Test split |

Each CSV must have the columns `text,label`, where `label` is `0` (negative)
or `1` (positive).

### Logging & Tracking

| Variable | Default | Description |
|----------|---------|-------------|
| `LOG_LEVEL` | `INFO` | Python log level |
| `LOG_FILE` | `training.log` | Log file path |
| `WANDB_API_KEY` | *(blank)* | Blank disables W&B |
| `WANDB_PROJECT` | `sentiment-classifier` | W&B project name |
| `WANDB_ENTITY` | *(blank)* | W&B team/user |

### Database (reserved)

`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` — reserved for
future use, not required yet.

---

## Project Structure

```
sentiment-classifier/
├── configs/
│   ├── model_config.yaml      # model settings (stub)
│   └── training_config.yaml   # training settings (stub)
├── data/                      # put train/val/test CSVs here (.gitkeep tracked)
├── models/                    # model artifacts (.gitkeep tracked)
├── src/
│   ├── config.py              # ✅ single source of truth for configuration
│   ├── train.py               # ⏳ stub
│   ├── evaluate.py            # ⏳ stub
│   └── utils/
│       ├── data_loader.py     # ⏳ stub
│       └── metrics.py         # ⏳ stub
├── tests/                     # ⏳ test files not written yet
│   ├── test_data_loader.py    # ⏳ stub (empty)
│   └── test_metrics.py        # ⏳ stub (empty)
├── .env.example               # documented config template (committed)
├── .env                       # your real secrets (gitignored)
├── .gitignore
├── requirements.txt           # production deps, pinned
├── requirements-dev.txt       # dev tools, pinned
├── requirements-frozen.txt    # exact environment snapshot
├── setup.sh                   # one-command environment setup
├── verify_setup.py            # environment self-check
└── test_env.py                # .env smoke test
```

---

## Testing

```bash
source venv/bin/activate
python -m pytest tests/ -v
```

Run with coverage:

```bash
python -m pytest tests/ --cov=src --cov-report=term-missing
```

---

## Environment Verification

```bash
python verify_setup.py
```

Checks Python version, virtual environment, required packages, project
structure, and Git configuration (including that `venv/` is gitignored).
Exits `0` on success, `1` on failure — suitable for CI.

---

## Git Hygiene

`.gitignore` excludes:

- `venv/`, `.venv/`, `env/` — virtual environments
- `.env`, `.env.local` — secrets (**never commit these**)
- `__pycache__/`, `*.pyc` — bytecode
- `*.pt`, `*.pth`, `*.h5`, `*.ckpt` — model weights
- `data/*.csv`, `data/*.json` — datasets
- `*.log`, `logs/`, `wandb/` — logs and experiment runs

`.env.example` **is** committed so others can see the required configuration.

---

## Project Status

| Area | Status |
|------|--------|
| Virtual environment & pinned dependencies | ✅ Complete |
| `.env` configuration + `src/config.py` | ✅ Complete |
| `setup.sh` automation | ✅ Complete |
| `verify_setup.py` self-check | ✅ Complete (all 5 checks pass) |
| Git repo + GitHub push | ✅ Complete |
| Unit tests (`tests/`) | ⏳ Not started (files are empty) |
| Data loading (`src/utils/data_loader.py`) | ⏳ Not started |
| Metrics (`src/utils/metrics.py`) | ⏳ Not started |
| Training loop (`src/train.py`) | ⏳ Not started |
| Evaluation (`src/evaluate.py`) | ⏳ Not started |
| YAML configs (`configs/*.yaml`) | ⏳ Not started |
| Dataset in `data/` | ⏳ Not started |

### Roadmap

1. Implement `src/utils/data_loader.py` — load and tokenize the CSV splits.
2. Implement `src/utils/metrics.py` — accuracy, precision, recall, F1.
3. Implement `src/train.py` — fine-tuning loop with validation.
4. Implement `src/evaluate.py` — test-set evaluation and reporting.
5. Wire up `configs/*.yaml` and add a CLI entry point.
6. Add a real dataset to `data/`.

---

## License

Add a license before publishing this repository publicly.
