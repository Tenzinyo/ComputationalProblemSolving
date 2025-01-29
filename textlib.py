"""
Example code from _Discovering Computer Science_, section 6.1
Author: Jessen Havill AND YOU
"""
import string
def removePunctuation(text):
    """Remove punctuation from a text.
    
    Parameter: text, a string object
    Return value: a copy of text with punctuation removed
    """
    newText = ''
    for character in text:
        if character not in string.punctuation:
            newText = newText + character
    return newText
def normalize(text):
    """Normalize a text by making it lowercase and removing punctuation.
    Parameter: text, a string object
    Return value: a normalized copy of text
    """
    newText = text.lower()
    newText = removePunctuation(newText)
    return newText
