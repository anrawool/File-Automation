from search import *
from sys import argv
import os
from config import get_shell_input

class Opener:
    def __init__(self, folder, target=None, mode=None):
        self.folder = folder
        self.target = target
        self.mode = mode
        if self.mode == 'folder':
            self.open_folders()
        else:
            self.open_files()
        
    def open_files(self):
        search_object = FileSearch(folder=self.folder, target=f'{target}', file_path=False)
        (files, folder_objs) = search_object.search()
        for folder_obj in folder_objs[0]:
            os.chdir(f'{folder_obj.path}')
            os.system(f'open {folder_obj.file + folder_obj.ext}')
    
    def open_folders(self):
        search_object = FileSearch(folder=self.folder, target=f'{target}', file_path=False)
        (folders, folder_objs) = search_object.search()
        print(folder_objs)
        for folder in folder_objs[0]:
            path = folder.path
            os.system(f'open {path}')



if __name__ == '__main__':
    folder, target = get_shell_input(1, argv, [''])
    if target == '' or '--' in target[0:2]:
        Opener(folder=folder, mode='folder')
        mode = 'folder'
    else:
        Opener(folder=folder, target=target)