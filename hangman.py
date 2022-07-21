import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' or ' ' in word:
        word = random.choice(words)

    return word 

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
user_input = input('type something:')
print(user_input)