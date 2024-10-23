from utils.function import add

def count_word(s, word):
    assert isinstance(s, str), "AssertionError"
    assert isinstance(word, str) and len(word) == 1, "AssentionError"


    count = 0
    for i in s:
        if(i == word):
            count = add(count, 1)
    
    return count

def hello():
    print("hello")