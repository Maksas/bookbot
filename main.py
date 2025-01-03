import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter +=1
    return counter

def count_letters(text):
    dict = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    return(dict)

def sort_on(dictonary):
    return dictonary[1]


def print_report():
    dictonary = count_letters(main())
    list_ = list(dictonary.items())
    list_.sort(reverse=True, key=sort_on)
    test = string.ascii_letters
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(main())} words found in the document")
    print("")
    for i in list_:
        if i[0] in test:
            print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")
    

print_report()