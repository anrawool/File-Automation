from search import *
from sys import argv
import os

class Opener:
    def __init__(self, folder, target=None, mode=None):
        self.folder = folder
        self.target = target
        self.mode = mode
        if self.mode != 'folder':
            self.open_files()
        else:
            self.open_folders()
        
    def open_files(self):
        search_object = FileSearch(folder=self.folder, target=f'{target}', file_path=False)
        (files, folder_objs) = search_object.search()
        folder_objs = folder_objs[0]
        files = files[0]
        for folder_obj in folder_objs:
            os.chdir(f'{folder_obj.path}')
            os.system(f'open {folder_obj.file + folder_obj.ext}')
    
    def open_folders(self):
        search_object = FileSearch(folder=self.folder, mode='folder')
        folder_objs = search_object.search()
        for folder in folder_objs:
            path = folder.path
            os.system(f'open {path}')



if __name__ == '__main__':
    folder = argv[1]
    try:
        target = argv[2]
        Opener(folder=folder, target=target)
    except IndexError:
        if len(argv) != 2:
            exit()
        else:
            mode = 'folder'
            Opener(folder=folder, mode='folder')