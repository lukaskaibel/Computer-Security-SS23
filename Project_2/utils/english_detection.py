import nltk
from nltk.corpus import words

# Download the word list if not already done
nltk.download("words")


def contains_english(text: str) -> bool:
    english_words = set(words.words())  # create a set for faster lookup
    text_words = text.lower().split()
    return any(word in english_words for word in text_words)
