from stats import count_words

def main():
    book = get_book_text("books/frankenstein_alt.txt")

    word_count = count_words(book)
    print(f"{word_count} words found in the document")


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


main()