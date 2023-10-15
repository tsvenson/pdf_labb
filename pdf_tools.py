from os import scandir


def find_pdfs_containing_string_in_name(search_string: str) -> None:
    number_of = 0
    for file_name in scandir('L:\Books'):
        if file_name.name.endswith('.pdf'):
            if search_string in file_name.name:
                print(file_name.name)
                number_of += 1
    print(f'\nI found {number_of} books with the string "{search_string}" in it.')
    return None

def main():
    search_files = input('Enter string to search in file name for: ').strip()
    if len(search_files) > 2:
        find_pdfs_containing_string_in_name(search_files)
    else:
        print('You need to type in at least 3 character!')

if __name__ == '__main__':
    main()