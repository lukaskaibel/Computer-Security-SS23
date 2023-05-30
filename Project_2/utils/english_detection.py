import nltk
from nltk.corpus import words

# Download the word list if not already done
nltk.download("words")


def contains_english(text: str) -> bool:
    english_words = set(words.words())  # create a set for faster lookup
    text_words = text.lower().split()
    english_word_count = 0
    for word in text_words:
        if (word in english_words) and (len(word) > 1):
            english_word_count +=1
    return english_word_count >= 3