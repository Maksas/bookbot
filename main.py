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
