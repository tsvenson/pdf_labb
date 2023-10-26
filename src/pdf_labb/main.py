import os

from rich import print
from pypdf import PdfReader

LIBRARY_PATH = os.environ['LIBRARY_PATH']


def find_pdfs_containing_string_in_name(search_string: str) -> list:
    matches = []
    for file_name in os.scandir(LIBRARY_PATH):
        if file_name.name.endswith('.pdf'):
            if search_string in file_name.name:
                matches.append(file_name.name)
    return matches


def select_book() -> str:
    search_files = input('Enter string to search in file name for: ').strip()
    if len(search_files) > 2:
        book_list = find_pdfs_containing_string_in_name(search_files)
    else:
        print('You need to type in at least 3 character!')
    
    for index, book in enumerate(book_list):
        print(index, book)
    book_choice = int(input('Select which book: ').strip())
    return book_list[book_choice]


def list_number_of_books_file_type() -> None:
    type_pdf: int = 0
    type_epub: int = 0
    type_mobi: int = 0
    type_other: int = 0

    for file_name in os.scandir(LIBRARY_PATH):
        if file_name.name.endswith('.pdf'):
            type_pdf += 1
        elif file_name.name.endswith('.epub'):
            type_epub += 1
        elif file_name.name.endswith('.mobi'):
            type_mobi += 1
        else:
            type_other += 1

    total = type_pdf + type_epub + type_mobi
    print(f'\nI found {total} PDF, EPUB and MOBI books in the libray.')
    print(f'PDF  : {type_pdf} books')
    print(f'EPUB : {type_epub} books')
    print(f'MOBI : {type_mobi} books')
    print(f'Other: {type_other} books')

    return None

def main():
    print('\nSelect what you want to do:')
    print('1 - List number of books in each file format.')
    print('2 - Select book with search string and print metadata.')
    print('0 - Quit')
    choice: int = int(input('Make choice: ').strip())
    match choice:
        case 0:
            print('By for now.')
        case 1:
            list_number_of_books_file_type()
        case 2:
            book = PdfReader(LIBRARY_PATH + '/' + select_book())
            print(book.metadata)
        case _:
            print('That was a wrong option!')

if __name__ == '__main__':
    main()