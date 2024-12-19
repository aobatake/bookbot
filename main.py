
def main():
    book_path = "books/frankenstein.txt"
    file_contents = None

    with open(book_path) as f:
        file_contents = f.read()

    words = file_contents.split()
    char_count = {}

    for word in words:
        l_word = word.lower()
        for char in l_word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    print(char_count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")

    print("--- End report ---")




main()
