from utils.count import hello
hello()

from utils.count import count_word

print("ここにはいる")

if __name__ == "__main__":
    s = "hello world"
    print("e:", count_word(s, 'e'))
    print("o:", count_word(s, 'o'))
    print("l:", count_word(s, 'l'))