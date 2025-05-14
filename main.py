import sys
from stats import get_book_text, count_words, count_char, pretty_sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
#    print(content)

    word_count = count_words(content)
#    print(f"{word_count} words found in the document")
    
    char_count = count_char(content)
#    for character, count in char_count.items():
#        print(f"''{character}': {count}'")
#    print(char_count)

    sorted_list = pretty_sort(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_list:
        if pair['char'].isalpha():
            print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")
    
main()
