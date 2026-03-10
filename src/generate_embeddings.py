import sys
import os
import json
from sentence_transformers import SentenceTransformer
from preprocessing import clean_text

# Ajouter le chemin racine pour trouver src
sys.path.append(os.path.abspath("."))


# Fichiers
raw_file = "/data/raw/jobs_raw.json"
clean_file = "/data/processed/jobs_clean.json"
embeddings_file = "/data/processed/jobs_embeddings.json"

os.makedirs("/data/processed", exist_ok=True)

# -------------------------------
# 1️⃣ Lire le JSON brut
# -------------------------------
with open(raw_file, encoding="utf-8") as f:
    jobs = json.load(f)

# -------------------------------
# 2️⃣ Nettoyer les descriptions
# -------------------------------
for job in jobs:
    job["clean_description"] = clean_text(job["description"])

# Sauvegarder les descriptions nettoyées
with open(clean_file, "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print(f"{len(jobs)} descriptions nettoyées et sauvegardées dans {clean_file}")

# -------------------------------
# 3️⃣ Générer les embeddings
# -------------------------------
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

for job in jobs:
    job["embedding"] = model.encode(job["clean_description"]).tolist()

# Sauvegarder les embeddings
with open(embeddings_file, "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print(f"Embeddings générés et sauvegardés dans {embeddings_file}")