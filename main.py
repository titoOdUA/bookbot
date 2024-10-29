def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    book_report(path, book_text)

def count_words(s):
    return len(s.split())

def count_characters(s):
    characters_dict = {}
    for c in s.lower():
        if c in characters_dict:
            characters_dict[c] += 1
        else:
            characters_dict[c] = 1
    return characters_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_char_dict_by_use(char_dict):
    return dict(sorted(char_dict.items(), key = lambda item: item[1], reverse = True))

def book_report(path, book_text):
    words_count = count_words(book_text)
    chars_dict = count_characters(book_text)
    sorted_dict = sort_char_dict_by_use(chars_dict)
    print(f"--- Begin report of {path} ---\n")
    print(f"{words_count} words found in the document")
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print(f"--- End report ---")


main()
