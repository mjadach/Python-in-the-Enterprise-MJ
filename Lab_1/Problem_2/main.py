import os

def list_all_files(folder_name):
    files_list = []
    for file in os.listdir(folder_name):
        if file.endswith(".log"):
            files_list.append(os.path.join((folder_name), file))
    return files_list

def clean_up_list(file):
    clean_word_list = []
    words_list = read_file(file)
    words_list.lower()
    new_words_list = words_list.split()
    symbols = "'1234567890~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
    for word in new_words_list:
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    return clean_word_list

def count_words_in_files(files_list):
    w=[]
    return w

def list_to_file(file_name, list_output):
    file = open(file_name, "w")
    for line in list_output:
        file.write(line)
        file.write("\n")
    file.close()

if __name__ == '__main__':
    folder_name = "Logs"
    file_name = "data.txt"
    files_list = list_all_files(folder_name)
    list_output = count_words_in_files(files_list)
    list_to_file(file_name, list_output)
    print("po zmianie")
    print("adasdasdsadaads")
    os.system("jupyter notebook ./" + file_name)
