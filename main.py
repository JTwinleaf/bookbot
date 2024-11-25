def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_of_char = get_char_count(text)
    list_of_char = dick_to_list(dict_of_char)
    sorted_charlist = sort_funk(list_of_char)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    get_char_report(sorted_charlist)
    print("--- End report ---")

def sorter(dictlist):
    return dictlist["count"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    count = {}
    characters = []
    lower_text = list(text.lower())
    for char in lower_text:
        if char.isalpha():
            characters.append(char)

    for char in characters:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def dick_to_list(dict):
    charList = []
    for key, value in dict.items():
        temp = {"char": key, "count": value}
        charList.append(temp)
    return charList

def sort_funk(dictlist):
    dictlist.sort(reverse=True, key=sorter)
    return dictlist

def get_char_report(chars):
    for char in chars:
        character = char["char"]
        count = char["count"]
        print(f"The {character} character was found {count} times")

main()