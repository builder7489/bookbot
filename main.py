from stats import count_words
from stats import count_chars
from stats import sort_chars

def main():
    book = "books/frankenstein_alt.txt"
    book_content = get_book_text(book)

    word_count = count_words(book_content)
    chars_count = count_chars(book_content)

    title = "BOOKBOT"
    line = "============"
    space = " "
    header = line+space+title+space+line
    
    print(header)
    print(f"Analyzing book found at {book}")
    print(f"{word_count} words found in the document")

    format_count = sort_chars(chars_count)

    for i in format_count:
        letter = i["char"]
        number = i["num"]

        if letter.isalpha():
            print(f"{letter}: {number}")

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


main()