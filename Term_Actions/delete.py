from search import FileSearcher
from sys import argv
import os
import sys
path = os.path.join('/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/')
sys.path.append(path)
from settings import get_shell_input
import shutil

in_folder, del_file = get_shell_input(2, argv)
search_method = FileSearcher(in_folder, del_file, file_path=False)
del_files, folder_objs = search_method.search()
for result in folder_objs:
    os.chdir(result.path)
    if result.file == None:
        sure = input(f'Are you sure you want to delete \'{result.folder}\'?')
    sure = input(f"Are you sure you want to delete \'{result.file}\' which is present in \'{result.folder}\'? [Y/n]: ")
    if sure == "Y":
        if result.ext != None:
            os.remove(f'{result.file+result.ext}')
        else:
            shutil.rmtree(f'{result.path}')
    else:
        pass
