import os
import json
from sentence_transformers import SentenceTransformer
from preprocessing import clean_text

 
# Définir le chemin racine du projet
 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_file = os.path.join(BASE_DIR, "data", "raw", "jobs_raw.json")
clean_file = os.path.join(BASE_DIR, "data", "processed", "jobs_clean.json")
embeddings_file = os.path.join(BASE_DIR, "data", "processed", "jobs_embeddings.json")

os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)

 
# Lire le JSON brut
 
with open(raw_file, encoding="utf-8") as f:
    jobs = json.load(f)

print(f"{len(jobs)} offres chargées")

# Nettoyer les descriptions
 
for job in jobs:
    job["clean_description"] = clean_text(job["description"])

with open(clean_file, "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print("Descriptions nettoyées sauvegardées")
 
# Charger le modèle embeddings

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Générer et sauvegarder les embeddings

for job in jobs:
    job["embedding"] = model.encode(job["clean_description"]).tolist()

with open(embeddings_file, "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print("Embeddings générés et sauvegardés")