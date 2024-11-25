def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    list_of_char = get_char_count(text)
    char_report = get_char_report(list_of_char)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(list_of_char)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    count = {}
    characters = list(text.lower())
    for char in characters:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def get_char_report(dict):
    pass

main()