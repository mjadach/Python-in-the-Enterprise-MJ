import os
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

from Lab_1.Problem_1_Grep import Exceptions


def list_all_files(folder_name):
    files_list = []
    for file in os.listdir(folder_name):
        if file.endswith(".log"):
            if validate_input_file(file_name) == 1:
                files_list.append(os.path.join((folder_name), file))
    return files_list


def find_in_files(files_list, string_to_look_for):
    list_output = []
    #variable so that you will not use first "info" row to visualise data
    first_line = 1
    for file in files_list:
        with open(file, "r") as f:
            for l in f:
                if l.find(string_to_look_for) != -1:
                    if first_line == 0:
                        list_output.append(l)
                    else:
                        first_line = 0
            first_line = 1
            list_output.append("\n\n")
    return list_output


def list_to_file(file_name, list_output):
    file = open(file_name, "w")
    for line in list_output:
        file.write(line)
        file.write("\n")
    file.close()


def validate_input_file(file_name):
    if not isinstance(file_name, str):
        raise Exceptions.NotAString()
    if not os.path.isfile(file_name):
        raise Exceptions.NotSuchFile()
    return True


def visualise(list_output):
    seperated_list = [i.split() for i in list_output]
    x_list = []
    y_list = []

    for x in seperated_list:
        iterator = 0
        for y in x:
            iterator += 1
            if iterator == 5:
                y_list.append(y)
            elif iterator == 7:
                x_list.append(y)

    pp = PdfPages('visualization.pdf')
    plt.plot(x_list, y_list, 'ro')
    plt.ylabel('tracks')
    plt.xlabel('from')
    plt.savefig(pp, format='pdf')
    pp.close()


if __name__ == '__main__':
    folder_name = "Logs"
    string_to_look_for = "PrChecker.Downs"
    file_name = "data.txt"
    files_list = list_all_files(folder_name)
    list_output = find_in_files(files_list, string_to_look_for)
    visualise(list_output)
    list_to_file(file_name, list_output)

    # to mi wyswietli w przegladarce plik tekstowy:
    # os.system("jupyter notebook ./" + file_name)
    # jak zrobic, zeby wyswietlalo tekst + wykres?
    # czyli jak polaczyc pdfa i txt sensownie?