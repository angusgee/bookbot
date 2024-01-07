def main():
        path = "./books/frankenstein.txt"
        text = get_book_contents(path)        
        num_words = calc_num_words(text)
        chars = count_letters(text)
        summary = summarise_word_count(chars)
        output = print_summary(summary, num_words)

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def calc_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def summarise_word_count(chars):
    char_list = []
    for key, value in chars.items():
        if key.isalpha():
            char_list.append((key, value))
    char_list.sort()
    return char_list

def print_summary(char_list, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} found in this document")
    for char in char_list:
        print(f"The '{char[0]}' character was found {char[1]} times")

if __name__ == "__main__":
    main()