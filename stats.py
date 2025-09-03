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
    #
    # [x] convert the book contents to lowercase
    # [x] build a set and add each unique value from the book contents
    # [x] iterate over the set to create the starting dictionary
    # [x] iterate through each character in book contents
    # [x] increase the corresponding value for each symbol key in the dictionary
    # [x] return dictionary

    to_lower = book_contents.lower()
    char_keys = set()
    count_of_chars = {}

    for char in to_lower:
        char_keys.add(char)
    
    for char in char_keys:
        count_of_chars[char] = 0

    for char in to_lower:
        count_of_chars[char] += 1 

    return count_of_chars