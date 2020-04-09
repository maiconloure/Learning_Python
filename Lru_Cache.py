from functools import lru_cache

@lru_cache(maxsize=None)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')


a = count_vowels('jogar')
print(a)