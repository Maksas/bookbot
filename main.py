def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter +=1
    return counter

print(count(main()))