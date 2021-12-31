list_file = ['1.txt', '2.txt', '3.txt']
def get_data_from_files(list_file: list) -> list:
    list_of_contents_of_all_files = []
    for file in list_file:
        strings_from_file = []
        with open(file, 'rt', encoding='utf-8') as source:
            for line in source:
                strings_from_file.append(line)
            strings_from_file.append(file)
            list_of_contents_of_all_files.append(strings_from_file)
    list_of_contents_of_all_files.sort()
    return list_of_contents_of_all_files

list_of_contents_of_all_files = get_data_from_files(list_file)


def write_overall_files_date_to_file(list_of_contents_of_all_files):
    with open('4.txt', 'wt', encoding='utf-8') as file:
        for i in range(len(list_of_contents_of_all_files)-1,-1,-1):
            file.write(f'{list_of_contents_of_all_files[i][-1]}\n{len(list_of_contents_of_all_files[i])-1}\n')
            for k in range(0, len(list_of_contents_of_all_files[i])-1):
                file.write(f'{list_of_contents_of_all_files[i][k]}')
            file.write('\n')

write_overall_files_date_to_file(list_of_contents_of_all_files)