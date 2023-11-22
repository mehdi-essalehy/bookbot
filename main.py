def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    letter_count = {}
    file_contents = file_contents.lower()
    for c in file_contents:
        if c in letter_count.keys():
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    return letter_count

def sort_on(d):
    return d[1]

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    letter_count = list(letter_count.items())
    letter_count.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for (c, count) in letter_count:
        if c.isalpha():
            print(f"The '{c}' character was found {count} times")