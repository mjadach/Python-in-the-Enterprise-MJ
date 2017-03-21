import os
from pprint import pprint
import Exceptions

def list_all_files(folder_name):
    files_list = []

    for file in os.listdir(folder_name):
        if file.endswith(".log"):
            if validate_input_file(folder_name + "\\" + file) == 1:
                files_list.append(os.path.join((folder_name), file))
# it shows error, and i dont know why - validator says there is no such file
    return files_list

def validate_input_file(file_name):
    if not isinstance(file_name, str):
        raise Exceptions.NotAString()
    if not os.path.isfile(file_name):
        raise Exceptions.NotSuchFile()
    return True

def clean_up_line(line):
    symbols = "'1234567890~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="

    line.lower()
    line.split()
    for char in symbols:
        line = line.replace(char, "")
    return line


def count_words_from_files(files_list):
    whole_file = []
    words = []
    for file in files_list:
        with open (file,"r") as f:
            for line in f:
                whole_file.append(clean_up_line(line))

    for line in whole_file:
        for word in line.split():
            words.append(word)

    words_counter = {}
    '''
    for word in words:
        words_counter[word] = words_counter.get(word, 0) + 1
    '''
    for word in words:
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1

    inverted_dict = dict([[v, k] for k, v in words_counter.items()])

    return inverted_dict


def dict_to_file(file_name, dict_output):
    with open(file_name, 'w') as out:
        pprint(dict_output, stream=out)


if __name__ == '__main__':
    folder_name = "Logs"
    file_name = "data.txt"
    files_list = list_all_files(folder_name)
    words_counter = count_words_from_files(files_list)
    dict_to_file(file_name, words_counter)
#    os.system("jupyter notebook ./" + file_name)
