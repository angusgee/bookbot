from stats import count_words, create_char_count_dict, create_dict_list
import sys

def get_args():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else: 
        return sys.argv[1]

def get_book_contents(path):
    with open(f'./books/{path}') as f:
        return f.read()

def print_output(path, word_count, dict_list):
    print('============ BOOKBOT ============\n')
    print(f'Analyzing book found at {path}...\n')
    print('----------- Word Count ----------\n')
    print(f'Found {word_count} total words\n')
    print('--------- Character Count -------\n')    
    for item in dict_list:  
        if item['name'].isalpha():
            print(f'{item['name']}: {item['num']}')
    print('============= END ===============')

def main():
    path = get_args()
    book_contents = get_book_contents(path) 
    word_count = (count_words(book_contents))
    char_count_dict = create_char_count_dict(book_contents)
    dict_list = create_dict_list(char_count_dict)
    print_output(path, word_count, dict_list)

if __name__ == "__main__":
    main()      