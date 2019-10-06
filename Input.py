import os
import shutil


def erase_blank_space(row):
    """*******************************************************"""
    """ Function erases(deletes) blank spaces from row given. """
    """                                                       """
    """ Funkcia vymaze medzery v riadku daneho na vstupe.     """
    """*******************************************************"""

    index = 0
    while index < len(row):
        row[index] = row[index].strip()
        if row[index] == " " or row[index] == "":
            del row[index]
        else:
            index += 1
    # print(row)
    # if len(row) > 0:
    #     row[-1] = row[-1][:-1]
    return row


def create_awards_assign(input_file2, awards):
    temp_awards = {}
    with open(input_file2, "r") as awards_info:
        for line in awards_info:
            line = line.split(";")
            awards[line[0]] = {"information": line[2]}
            assignment = line[3].split("+")
            for criteria in range(len(assignment) - 1):
                temp_awards[assignment[criteria]] = line[0]
            temp_awards[assignment[-1][:-1]] = line[0]
    return temp_awards


def create_objective_assign(objectives_input):
    temp_objectives = {}
    with open(objectives_input, "r") as objectives_input_file:
        for line in objectives_input_file:
            line = line.split(";")
            if "\n" in line[2]:
                line[2] = line[2][:-1]
            temp_objectives[line[0]] = {"points": int(line[1]), "gametype": line[2]}
    return temp_objectives


def process_configuration_line(config_file, line_index):
    temp_var = config_file.readline()
    temp_var = temp_var.split(";")
    if len(temp_var) != 2:
        print("Nespravny pocet argumentov (chybajuci riadok) v {}.riadku suboru './config.txt'".format(line_index))
        return -1
    if "\n" in temp_var[1]:
        temp_var[1] = temp_var[1][:-1]
    return temp_var[1]


def get_configuration(file_path, temp_wincount):
    with open(file_path, "r") as config:

        # Zisti nazov priecinku pre ulozenie vystupu
        tem_dir_name = process_configuration_line(config, 1)
        if tem_dir_name == -1:
            return -1, -1, -1, -1
        if not os.path.exists(tem_dir_name):
            os.makedirs(tem_dir_name)
        else:
            shutil.rmtree(tem_dir_name)
            os.makedirs(tem_dir_name)

        # Zisti body na vyhru v RETRIEVAL
        temp_wincount["re"] = {"axis": 0, "allies": 0, "limit": int(process_configuration_line(config, 2))}
        if temp_wincount["re"]["limit"] == -1:
            return -1, -1, -1, -1

        # Zisti body na vyhru v SEARCH & DESTROY
        temp_wincount["sd"] = {"axis": 0, "allies": 0, "limit": int(process_configuration_line(config, 3))}
        if temp_wincount["sd"]["limit"] == -1:
            return -1, -1, -1, -1

        # Zisti vypisovany pocet najlepsich hracov pre kazdy AWARD
        temp_awards_top = int(process_configuration_line(config, 4))
        if temp_awards_top == -1:
            return -1, -1, -1, -1

        # Zisti nazov suboru s logom
        log_file_name = process_configuration_line(config, 5)
        if log_file_name == -1:
            return -1, -1, -1, -1

    return tem_dir_name, temp_wincount, temp_awards_top, log_file_name


def get_aliases(inputfilename):
    temp_aliases = {}
    with open(inputfilename, "r") as inputfile:
        for line in inputfile:
            line = line[:-1].split(";")
            for alias in line:
                if not (alias in temp_aliases):
                    temp_aliases[alias] = line[0]
    return temp_aliases
