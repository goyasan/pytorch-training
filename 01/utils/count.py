def count_word(str, word):
    count = 0
    for i in str:
        if(i == word):
            count = count + 1
    
    return count

def hello():
    print("hello")