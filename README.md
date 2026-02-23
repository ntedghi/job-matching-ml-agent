# Job Matching ML Agent

A lightweight, production-oriented machine learning agent that matches job seekers to relevant job postings using text embeddings and semantic search.

## Project Structure

```
job-matching-ml-agent/
├── data/
│   ├── raw/          # Raw, unprocessed datasets
│   └── processed/    # Cleaned and feature-engineered data
├── src/
│   └── preprocessing.py  # Text cleaning utilities
├── notebooks/        # Exploratory data analysis notebooks
├── app/              # Streamlit front-end (coming soon)
├── requirements.txt
└── README.md
```

## Quickstart

```bash
pip install -r requirements.txt
```

## Roadmap

- [x] Project scaffolding and text preprocessing module
- [ ] Data ingestion pipeline (job postings + resumes)
- [ ] Text vectorisation with TF-IDF / sentence embeddings
- [ ] FAISS-based semantic similarity search
- [ ] Candidate ranking and scoring
- [ ] Streamlit demo app

