from stats import count_words, count_chars

def get_book_contents(path):
    with open(path) as f:
        return f.read()



def main():
    path = './books/frankenstein.txt'
    book_contents = get_book_contents(path)
    print('{} words found in the document'.format(count_words(book_contents)))
    char_count = count_chars(book_contents)
    print(char_count    )

if __name__ == "__main__":
    main()      