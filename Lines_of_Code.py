import os
from tabulate import tabulate
import re

def main():
    folder = "/workspaces/99223872/"                                                                                #   Initial parent folder
    paths, files  = get_files_and_pathes(folder)                                                                    #   returns list of files and paths
    fixed_files  = fix_path_lists(files)                                                                            #   returns list only python files
    fixed_paths  = fix_path_lists(paths)                                                                            #   returns list of python file pathes
    header_tabulate = ["Files 1","Files 2","Files 3","Files 4","Files 5"]                                           #   tabulate header
    print(tabulate(make_list_tabulate(fixed_files), headers=header_tabulate, tablefmt="grid"))                      #   print table
    users_file = input("Select file name from the table. ")                                                         #   ask file name
    ind = fixed_files.index(users_file)                                                                             #   get file name index from the list
    with open(fixed_paths[ind],"r") as file:                                                                        #   open and read file and get lines
        lines = file.readlines()
    result_lines = count_loc(lines)                                                                                 #   get code lines from file
    print(f"File {users_file} contains {result_lines} lines. File is in {fixed_paths[ind]} folder")                 #   print answer with number of code lines, name of file and path of file

def count_loc(lines):                                                                                               #   function for count only code lines
    nb_lines = 0
    docstring = False
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#") or docstring and not (line.startswith('"""')\
        or line.startswith("'''")) or (line.startswith("'''") and line.endswith("'''") and len(line) > 3)\
        or (line.startswith('"""') and line.endswith('"""') and len(line) > 3):
            continue
        elif line.startswith('"""') or line.startswith("'''"):
            docstring = not docstring
            continue
        else:
            nb_lines += 1
    return nb_lines

def make_list_tabulate(list):                                                                                       #   function to create table with list 5 columns
    tabulate_list = []
    temp_list = []
    counter = 0
    last_temp_list = []
    for i in list:
        temp_list.append(i)
        counter += 1
        if counter == 5:
            tabulate_list.append(temp_list)
            temp_list = []
            counter = 0
        if (len(list) - len(tabulate_list)*5) < 5:
            last_temp_list.append(i)
    tabulate_list.append(last_temp_list)
    return tabulate_list


def get_files_and_pathes(dirname):                                                                                  #   function to get files and pahtes
    files =[]
    pathes = []
    path_for_Find = []
    for i in os.listdir(dirname):
        if os.path.isdir(dirname + i):
            pathes.append(dirname + i)
    for k in pathes:
        for j in os.listdir(k):
            files.append(j)
            path_for_Find.append(k+"/"+j)
    return path_for_Find, files

def fix_path_lists(list):                                                                                           #   function get only python files and pathes
    py_pattern = (r"[a-zA-z0-9/_]\.py$")
    pathList = []
    for j in list:
        if re.compile(py_pattern).search(j) and j != "":
            pathList.append(j)
    return pathList

if __name__ == "__main__":
    main()
