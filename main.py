from stats import count_words

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def main():
    path = './books/frankenstein.txt'
    # print(get_book_contents(path))
    book_contents = get_book_contents(path)
    print('{} words found in the document'.format(count_words(book_contents)))

if __name__ == "__main__":
    main()      