def count_words(book_contents):
    return len(book_contents.split())

def count_chars(book_contents):
    char_dict = {}
    for char in book_contents:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        elif char.lower() in char_dict:
            char_dict[char.lower()] += 1
    return char_dict

print(count_chars('this is a test str'))
print(count_chars('aAAAAbcdefgh12345'))