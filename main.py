from stats import count_words
from stats import count_chars

def main():
    book = get_book_text("books/frankenstein_alt.txt")

    word_count = count_words(book)
    print(f"{word_count} words found in the document")

    # testing counting characters feature
    chars_count = count_chars(book)

    for char in chars_count:
        print(f"{char}:{chars_count[char]}")

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


main()