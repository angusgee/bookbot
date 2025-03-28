def count_words(book_contents):
    return len(book_contents.split())

def create_char_count_dict(book_contents):
    char_dict = {}
    for char in book_contents:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        elif char.lower() in char_dict:
            char_dict[char.lower()] += 1
    return char_dict

def sort_on(dict):
    return dict['num']

def create_dict_list(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        dict_list.append({'name': key, 'num': value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


# print(create_dict_list((create_char_count_dict('this is a test str'))))
# print(create_dict_list((create_char_count_dict('aAAAAbcdefgh12345'))))
