from os import scandir


LIBRARY_PATH = 'L:\Books'


def find_pdfs_containing_string_in_name(search_string: str) -> None:
    number_of: int = 0
    for file_name in scandir(LIBRARY_PATH):
        if file_name.name.endswith('.pdf'):
            if search_string in file_name.name:
                print(file_name.name)
                number_of += 1
    print(f'\nI found {number_of} books with the string "{search_string}" in it.')
    return None

def main():
    print('\nSelect what you want to do:')
    print('1 - List number of books in each file format.')
    print('2 - List books where the filename contains a specific string.')
    print('0 - Quit')
    choice: int = int(input('Make choice: ').strip())
    match choice:
        case 0:
            print('By for now.')
        case 1:
            print('Comming soon.')
        case 2:
            search_files = input('Enter string to search in file name for: ').strip()
            if len(search_files) > 2:
                find_pdfs_containing_string_in_name(search_files)
            else:
                print('You need to type in at least 3 character!')
        case _:
            print('That was a wrong option!')

if __name__ == '__main__':
    main()