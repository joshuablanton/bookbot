import sys
from stats import word_count
from stats import get_character_count
from stats import sort_char_count

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    char_count = sort_char_count(get_character_count(book_text))
    #print(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()