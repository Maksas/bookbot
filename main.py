import string
import sys
from stats import *

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents


def print_report():
    dictonary = count_letters(main())
    list_ = list(dictonary.items())
    list_.sort(reverse=True, key=sort_on)
    test = string.ascii_letters
    print(f"--- Begin report of books {sys.argv[1]} ---")
    print(f"{count_words(main())} words found in the document")
    print("")
    for i in list_:
        if i[0] in test:
            print(f"{i[0]}: {i[1]}")
    print("--- End report ---")
    

print_report()