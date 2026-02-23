# preprocessing.py
# Basic text cleaning utilities for job descriptions and resumes.

import string

import nltk
from nltk.corpus import stopwords

# Download stopwords only if not already present
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

_STOP_WORDS = set(stopwords.words("english"))


def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def remove_punctuation(text: str) -> str:
    """Remove punctuation characters from text."""
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_stopwords(text: str) -> str:
    """Remove common English stopwords from whitespace-tokenised text."""
    tokens = text.split()
    filtered = [word for word in tokens if word not in _STOP_WORDS]
    return " ".join(filtered)


def clean_text(text: str) -> str:
    """Apply full cleaning pipeline: lowercase → remove punctuation → remove stopwords."""
    text = to_lowercase(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    return text
