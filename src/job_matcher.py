import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Chemins
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jobs_file = os.path.join(BASE_DIR, "data", "processed", "jobs_embeddings.json")


# Charger les jobs
with open(jobs_file, encoding="utf-8") as f:
    jobs = json.load(f)

print(f"{len(jobs)} jobs chargés")


# Charger modèle embeddings
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


# CV utilisateur
cv_text = """
Machine learning and IA engineer with strong Python skills.
Experience with deep learning, data analysis and model deployment.
Worked with TensorFlow, PyTorch and large datasets.
"""

# embedding du CV
cv_embedding = model.encode(cv_text)


# Calcul similarité

results = []

for job in jobs:

    job_embedding = np.array(job["embedding"])

    score = cosine_similarity(
        [cv_embedding],
        [job_embedding]
    )[0][0]

    results.append((score, job))


# Trier résultats
results.sort(reverse=True, key=lambda x: x[0])

# Afficher top jobs
threshold = 0.65

print("\nMatching jobs:\n")

for score, job in results:

    if score >= threshold:

        print(job["title"])
        print(job["company"])
        print("score:", round(score, 3))
        print()