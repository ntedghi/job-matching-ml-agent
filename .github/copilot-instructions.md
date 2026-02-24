<!-- Copilot / AI agent instructions tailored to this repository -->
# Copilot instructions for `job-matching-ml-agent`

But: donner à un agent IA le contexte minimal pour être productif dans ce dépôt.

Résumé rapide
- **Projet**: `job-matching-ml-agent` — "ML-based job matching agent using embeddings and RAG architecture" (voir `README.md`).

Ce qu'il faut savoir en premier
- Le dépôt est très léger aujourd'hui : seul `README.md` existe et décrit l'intention (embeddings + RAG).
- Actions sûres : ne pas deviner l'architecture complète — proposer des fichiers/placements concrets et demander validation avant d'implémenter.

Objectifs pour l'agent
- Scanner le dépôt pour trouver code, configs, tests avant tout changement.
- Quand l'information manque, créer des fichiers _scaffolding_ (`src/`, `tests/`, `requirements.txt` ou `pyproject.toml`) et demander approbation.

Architecture attendue (déduite)
- Composants probables :
  - `ingest/` : scripts pour ingérer offres et CVs en texte.
  - `embeddings/` : code d'encodage (OpenAI, HuggingFace, etc.).
  - `vectorstore/` : wrapper pour base de vecteurs (FAISS, Milvus, Pinecone).
  - `rag/` : pipeline de retrieval + génération.
  - `agent/` : orchestration et API CLI.

Règles pratiques pour modifications
- Toujours référencer `README.md` quand on motive une modification architecturale.
- Si vous ajoutez une dépendance Python, préférez `pyproject.toml` (PEP 621) ou `requirements.txt` au besoin et fournissez la commande d'installation Windows PowerShell :

```
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

Exemples concrets (à utiliser comme templates)
- Ajouter ingestion minimal : créer `src/ingest/__init__.py` et `src/ingest/reader.py` avec une fonction `read_documents(path) -> List[str]`.
- Ajouter wrapper embeddings : `src/embeddings/client.py` avec interface `embed(texts: List[str]) -> List[List[float]]`.
- Ajouter interface vectorstore : `src/vectorstore/interface.py` décrivant `upsert(docs)`, `search(query, k)`.

Commit / PR conventions
- Branch: ouvrir une branche courte `feat/<what>` ou `fix/<what>`.
- Message de commit : `<scope>: <bref résumé>` suivi de détails si utile.
- PR title : `feat: add <short description>` et dans la description l'artefact ajouté (fichiers, endpoints, commandes pour reproduire).

Quand tu n'es pas sûr
- Pose une question claire et ciblée dans l'issue/PR ou ici avant d'implémenter.
- Si l'utilisateur ne répond pas, crée un petit prototype non destructif (nouveau dossier `draft/`), documente son usage dans `README.md` et demande revue.

Fichiers clés à vérifier avant travail
- `README.md` (racine) — seul point d'entrée fiable aujourd'hui.
- Tout fichier nouvellement ajouté sous `src/`, `tests/`, `pyproject.toml`, `requirements.txt`.

Ne pas faire
- Ne pas supprimer ou refactorer du code existant sans tests ou sans approbation.

Demande de feedback
- Après la PR initiale, demander explicitement : "Valide-tu ces emplacements et conventions (ingest/embeddings/vectorstore)?".

Fin.