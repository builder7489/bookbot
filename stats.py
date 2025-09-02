def count_words(book_contents):
    # get book contents
    # split the contents into a list
    # count the list length plus one
    words = book_contents.split()

    count = len(words)
    
    return count

def count_chars(book_contents):
    # takes contents of book as string
    # returns the count of each character including symbols and spaces
    # convert any character to lowercasea
    # use a dictionary of string -> integers for the storing the counts of each character

    