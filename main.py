from stats import get_num_words, get_letter_frequency, get_char_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    num_words = get_num_words(text)
    letter_frequency = get_letter_frequency(text)
    sorted_char_freq =  get_char_counts(letter_frequency)


    for item in sorted_char_freq:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    print("============= END ===============")
    print(sys.argv)

main()