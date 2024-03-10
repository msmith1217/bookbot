import string

def main():
    filepath = "books/frankenstein.txt"
    book_name = filepath.split("/")[-1]
    with open(filepath) as f:
        file_contents=f.read()
    words = file_contents.split()
    lower_book = file_contents.lower()
    print(len(words))
    dict = {letter: 0 for letter in string.ascii_lowercase}
    for letter in lower_book:
        if letter in dict:
            dict[letter] += 1
    print(f"---Begin report of {book_name}---")
    print(f"The book has {len(words)} words")
    for key in dict:
        print(f"The {key} character appears {dict[key]} times in the book")
    print(f"---End report of {book_name}---")






if __name__ == "__main__":
    main()