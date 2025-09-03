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

    to_lower = book_contents.lower()
    count_of_chars = {}

    for char in to_lower:
        if char in count_of_chars:
            count_of_chars[char] += 1
        else:
            count_of_chars[char] = 1

    return count_of_chars

# Adding helper function for sorting dictionaries
# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_with(characters):
    return characters["num"]

# using a dictionary of characters with their counts i.e. {"a": 9, "b": 8, "c": 7}
# return a list of sorted dictionaries in the following format i.e. [{"char": "z", "num": 765}]
def sort_chars(characters):
    # format each dictionary iteration into a new dictionary
    # append the new dict to the list
    format_chars = []

    for chars in characters:
        letter = chars
        number = characters[chars]

        to_add = {
            "char": letter,
            "num": number,
        }

        format_chars.append(to_add)

    format_chars.sort(reverse=True, key=sort_with)

    return format_chars