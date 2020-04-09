import re

def is_isogram(string):
    string = re.sub(r"[^A-Za-z0-9]+", "", string).lower()
    print(string)
    print(set(string))
    return len(set(string)) == len(string)


if __name__ == '__main__':
    test1 = 'Alphabet'
    test2 = 'six-year-old'
    print(is_isogram(test1))
    print(is_isogram(test2))