# python-projects
# Real-time GenAI pipeline

## Problem statement
The goal is to build a minimal, reproducible pipeline that ingests tabular data, trains a baseline model, and exposes a tiny FastAPI prediction service. This acts as a foundation you can evolve into real-time GenAI use cases (e.g., feature engineering, embeddings, or re-ranking).

## Data link
Source: <PUT_YOUR_DATA_URL_HERE>  
Format: CSV (rows = samples, columns = features, target = "label").  
If no public link exists, place raw.csv in data/.

## Design
- Ingestion: Load CSV from data/raw.csv or download via script.
- Training: Scikit-learn Pipeline with preprocessing and a simple classifier.
- Persistence: Save fitted pipeline to models/model.pkl.
- Serving: FastAPI exposes /health and /predict.
- Reproducibility: Single script in notebooks/01_data_and_training.py with deterministic seeds.

## Assumptions
- Data includes a column named label as the target.
- Mixed numeric and categorical features are possible.
- No missing values beyond simple imputation needed.
- Baseline metrics are sufficient for initial evaluation; further tuning is out of scope.

## How to run
1. Create environment:

