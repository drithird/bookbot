from curses.ascii import isalpha


def count_letters(text: str):
    letter_count = {}
    for letter in text:
        if letter.lower() in letter_count and letter.isalpha():
            letter_count[letter.lower()] += 1
        elif letter.isalpha():
            letter_count[letter.lower()] = 1 
        else:
            pass
    return letter_count
        
       

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = 0
        for word in words:
            total_words += 1
        print(total_words) 
        data = count_letters(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        for letter in data:
            
            print(f"The '{letter}' character was found {data[letter]} times")
        
        print("--- End report ---")  
        
main()

