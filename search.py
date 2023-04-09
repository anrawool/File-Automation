import os
from sys import argv
from data import *
import re
import settings
from settings import get_shell_input


class FileSearcher():
    def __init__(self, folder : str, target : str = '', mode : str = '', file_path : bool = True) -> None:
        # Initializing inputs along with preformatting
        self.inputs = [self.sterilize(folder), target.lower(), mode, file_path] # Undused Variables to be used in the future
        self.DataMaker = DataMaker()
        # Setting function variable
        self.function = self.get_function(self.inputs[1])
        self.control = False
        self.sub_folders = []
        self.results = []
    
    def get_function(self, target : str) -> str:
        """Sets the type of function to be used in conjunction with the search_folder function"""
        if "." in target:
            function = 'ext'
        elif "--all-folders" == target:
            function = 'all_folders'
        elif '--all-files' == target:
            function = 'all_files'
        else:
            function = 'name'
        return function


    def sterilize(self, ster_str: str) -> str:
        """Easy Normalizer for all inputs and outputs of the FileSearcher script"""
        # Replacing all spaces and extra underscores with only underscores
        str_obj = re.sub(" +", "_", ster_str)
        str_obj = re.sub("_+", "_", ster_str)
        str_obj = re.sub("/+", "/", ster_str)
        return str_obj.lower() # Final Normalization
    
    def check_parents(self, folders : list) -> None:
        """Sets the first iteration folder list for the program"""
        if self.inputs[0] in folders:
            self.inputs[0] = ''
        # Setting Parent Folders List Using Custom Data-type
        self.folders = list(map(lambda x: self.DataMaker.make_folder_path(f'{settings.ROOT_DIR}{x}', file_path=self.inputs[3]), folders))
        self.folders = list(map(lambda x: self.DataMaker.make_folder_path(f'{settings.ROOT_DIR}{x}', file_path=self.inputs[3]), folders))
        # print("Parents:", self.folders)
        for parent in self.folders:
            # Path Normalization
            sterilized_search = self.sterilize(parent.folder)
            if self.inputs[0] == sterilized_search:
                print("Found!!")
                self.results.append(parent)
            else:
                pass
    
    def trim(self, item_list : list, mode : str = 'folders') -> list:
        """Gets valid folders out of a list passed into the function"""
        if mode != 'folders':
            temp_files = [file.name for file in item_list if '.' in file.name]
            return temp_files
        self.ignore_folders = ['Public', 'Movies', 'Applications', 'opt', 'Library', 'Desktop', 'Pictures', 'Music', 'Sites'] # Restricted Folders
        # List comprehension for getting all folders not in the ignore list
        temp_folds = [folder.name for folder in item_list if '.' not in folder.name and folder.name not in self.ignore_folders]
        return temp_folds

    def check_with_result(self, object: str, target: str) -> bool:
        if self.sterilize(object) in self.sterilize(target):
            return True
        else:
            return False

    def change_for_results(self, object : NexusFolderPathObject):
        object.path = os.path.join(object.path, self.inputs[0])
        object.folder = self.inputs[0]
        return object

    def search_folder(self) -> list:
        """Searches Folder location on the computer files and returns complete details"""
        self.folders = os.scandir(f'{settings.ROOT_DIR}') # Root Directory Scan
        self.folders = self.trim([folder for folder in self.folders]) # Folder Extraction
        self.folders = [parent for parent in self.folders] # Setting Folders into a list
        # Checking Parent Exceptions
        self.check_parents(self.folders)
        while self.control != True:
            try:
                for parent_dir in self.folders:
                    subdirectories = [dir for dir in os.scandir(f'{parent_dir.path}/')]
                    subdirectories = self.trim(subdirectories)
                    for sub_directory in subdirectories:
                        sterilized_search = self.sterilize(sub_directory)
                        if self.check_with_result(self.inputs[0], sterilized_search):
                            # Result Formatting Function
                            each_folder_changed = self.change_for_results(parent_dir)
                            self.results.append(each_folder_changed)
                        self.sub_folders.append(self.DataMaker.make_folder_path(f'{parent_dir.path}/{sub_directory}', file_path=self.inputs[3]))
                self.folders = self.sub_folders # Setting up for next iteration
                self.sub_folders = [] # Resetting the Sub folders list for easy transition
            except Exception:
                pass
                self.control = True
        return self.results
    
    def convert_scan(self, scanned: list) -> list:
        scanned = [item.name for item in scanned]
        return scanned
    
    def name(self):
        item_names = []
        item_objects = []
        target = self.inputs[1]
        paths = [object.path for object in self.results]
        for path in paths:
            items = self.convert_scan(list(os.scandir(path)))
            for item in items:
                if target == item:
                    item_names.append(item)
                    item_objects.append(self.DataMaker.make_folder_path(f'{path}/{item}', file_path=self.inputs[3]))
        return item_names, item_objects


                



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
