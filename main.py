from stats import count_words
from stats import count_chars
from stats import sort_chars

def main():
    book = "books/frankenstein.txt"
    book_content = get_book_text(book)

    word_count = count_words(book_content)
    chars_count = count_chars(book_content)

    app_title = "============ BOOKBOT ============"
    word_title = "----------- Word Count ----------"
    char_title = "--------- Character Count -------"
    end_title = "============= END ==============="

    print(f"{app_title}\nAnalyzing book found at {book}...")
    print(f"{word_title}\nFound {word_count} total words")
    print(f"{char_title}")

    format_count = sort_chars(chars_count)

    for i in format_count:
        letter = i["char"]
        number = i["num"]

        if letter.isalpha():
            print(f"{letter}: {number}")
    
    print(f"{end_title}")

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


main()