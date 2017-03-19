    import os

def list_all_files(folder_name):
    files_list = []
    for file in os.listdir(folder_name):
        if file.endswith(".log"):
            files_list.append(os.path.join((folder_name), file))
    return files_list

def find_in_files(files_list, string_to_look_for):
    list_output = []
    for file in files_list:
        with open(file, "r") as f:
            list_output.append(file + ":\n\n")
            for l in f:
                if l.find(string_to_look_for) != -1:
                    list_output.append(l)
            list_output.append("\n\n")
    return list_output

def list_to_file(file_name, list_output):
    file = open(file_name, "w")
    for line in list_output:
        file.write(line)
        file.write("\n")
    file.close()

if __name__ == '__main__':
    folder_name = "Logs"
    string_to_look_for = "PrChecker.Downs"
    file_name = "data.txt"
    files_list = list_all_files(folder_name)
    list_output = find_in_files(files_list, string_to_look_for)
    list_to_file(file_name, list_output)
    os.system("jupyter notebook ./" + file_name)

    #jak zobrazować wyjście??