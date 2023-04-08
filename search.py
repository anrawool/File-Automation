import os
from sys import argv
from data import *
import re
from config import get_shell_input


class FileSearcher():
    def __init__(self, folder, target='', mode='', file_path=True):
        # Initializing inputs along with preformatting
        self.inputs = [self.sterilize(folder), target.lower(), mode, file_path]
        self.DataMaker = DataMaker()
        # Setting function variable
        self.function = self.get_function(self.inputs[1])
        self.control = False
        self.sub_folders = []
        self.results = []
    
    def get_function(self, target):
        if "." in target:
            function = 'ext'
        elif "--all-folders" == target:
            function = 'all_folders'
        elif '--all-files' == target:
            function = 'all_files'
        else:
            function = 'name'
        return function


    def sterilize(self, ster_str):
        # Replacing all spaces and extra underscores with only underscores
        str_obj = re.sub(" +", "_", ster_str)
        str_obj = re.sub("_+", "_", ster_str)
        return str_obj.lower() # Final Normalization
    
    def check_parents(self, folders):
        """Sets the first iteration folder list for the program"""
        if self.inputs[0] in folders:
            self.inputs[0] = ''
        # Setting Parent Folders List Using Custom Data-type
        self.folders = list(map(lambda x: self.DataMaker.make_folder_path(f'/Users/abhijitrawool/{x}'), folders))
        # print("Parents:", self.folders)
        for parent in self.folders:
            # Path Normalization
            sterilized_search = self.sterilize(parent.folder)
            if self.inputs[0] == sterilized_search:
                print("Found!!")
                self.results.append(parent)
            else:
                pass
    
    def folder_trim(self, folder_list):
        self.ignore_folders = ['Public', 'Movies', 'Applications', 'opt', 'Library', 'Desktop', 'Pictures', 'Music', 'Sites']
        # List comprehension for getting all folders not in the ignore list
        temp_folds = [folder.name for folder in folder_list if '.' not in folder.name and folder.name not in self.ignore_folders]
        return temp_folds

    def check_with_result(self, object, target):
        if self.sterilize(object.folder) in target:
            return True
        else:
            return False

    def change_for_results(self, object):
        object.path += '/' + self.inputs[0]
        object.folder = self.inputs[0]
        return object

    def search_folder(self):
        self.folders = os.scandir('/Users/abhijitrawool/')
        self.folders = self.folder_trim([folder for folder in self.folders])
        self.folders = [parent for parent in self.folders]
        print(self.folders)
        self.check_parents(self.folders)
        while self.control != True:
            try:
                for each_folder in self.folders:
                    directories = [dir for dir in os.scandir(f'{each_folder.path}/')]
                    directories = self.folder_trim(directories)
                    for each_dir in directories:
                        sterilized_search = self.sterilize(each_dir)
                        if self.inputs[0] == sterilized_search:
                            each_folder_changed = self.change_for_results(each_folder)
                            self.results.append(each_folder_changed)
                        self.sub_folders.append(self.DataMaker.make_folder_path(f'{each_folder.path}/{each_dir}'))
                self.folders = self.sub_folders
                self.sub_folders = []
                # Script Ready!
            except Exception:
                pass
                self.control = True
        return self.results



def find(folder, target='', mode=''):
    if mode == '':
        search_instance = FileSearcher(folder, target)
    else:
        search_instance = FileSearcher(folder, mode=mode)
    results = search_instance.search_folder()
    return results
if __name__ == '__main__':
    folder, target = get_shell_input(1, argv, exceptions=[''])
    if target == '':
        mode = 'folder'
    else:
        mode = ''
    res = find(folder, target, mode)
    print(res)
