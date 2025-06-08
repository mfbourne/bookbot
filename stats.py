def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    number_of_words = len(get_book_text("books/frankenstein.txt").split())
    return number_of_words

def count_characters():

