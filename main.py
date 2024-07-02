def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    generate_report(book_path, num_words, num_chars)


def get_num_chars(text):
    text = text.lower()
    chars_count = { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

    for char in text:
        print()
        if chars_count.get(char) != None:
            chars_count[char] += 1

    return chars_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def generate_report(book_path, num_words, num_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n");

    for char, count in sorted(num_chars.items(), reverse=True, key=lambda dict: dict[1]):
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()