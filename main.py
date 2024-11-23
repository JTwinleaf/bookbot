with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    number_of_words = len(words)
    print(number_of_words)