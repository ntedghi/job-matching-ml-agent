# preprocessing.py
# Basic text cleaning utilities for job descriptions and resumes.

import string
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are available
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

# English + French stopwords
STOP_WORDS = set(stopwords.words("english")) | set(stopwords.words("french"))


def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    if not text:
        return ""
    return text.lower()


def remove_punctuation(text: str) -> str:
    """Remove punctuation characters from text."""
    if not text:
        return ""
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_stopwords(text: str) -> str:
    """Remove common English and French stopwords."""
    if not text:
        return ""

    tokens = text.split()
    filtered_tokens = [word for word in tokens if word not in STOP_WORDS]

    return " ".join(filtered_tokens)


def clean_text(text: str) -> str:
    """
    Apply full cleaning pipeline:
    lowercase → remove punctuation → remove stopwords
    """
    text = to_lowercase(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)

    return text.strip()