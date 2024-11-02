def main():
    book_path = "books/frankenstein.txt"
    print("--- Begin report of books/frankenstein.txt ---")
    book = get_book_text(book_path)
    words(book)
    chars_dict = count_characters(book)
    chars_list = get_list(chars_dict)
    report(chars_list)
    
def words(book):
    words = book.split()
    length_of_words = len(words)
    print(f"{length_of_words} words found in the document\n")

def count_characters(book):
    chars_dict = {}
    for c in book:
        lowered = c.lower()
        if(lowered in chars_dict):
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

def get_list(chars_dict):
    new_list = []
    for c in chars_dict:
        new_list.append({"key": c, "value": chars_dict[c]})
    return new_list

def sort_on(item):
    return item["value"]

def report(list_dict):
    list_dict.sort(reverse = True, key=sort_on)
    for i in list_dict:
        if(i["key"].isalpha()):
            print(f"The '{i["key"]}' character was found {i["value"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

