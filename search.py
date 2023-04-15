import os
from sys import argv
from data import *
import re
import settings
from settings import get_shell_input
import time

class FileSearcher():
    def __init__(self, folder: str, target: str = '', mode: str = '', file_path: bool = True, record_time : bool = False) -> None:
        self.record_time = record_time
        if self.record_time == True:
            self.start = time.time()
        # Initializing inputs along with preformatting
        # Undused Variables to be used in the future
        self.inputs = [self.sterilize(folder), target.lower(), mode, file_path]
        self.DataMaker = DataMaker()
        # Setting function variable
        self.function = self.get_function(self.inputs[1])
        self.control = False
        self.sub_folders = []
        self.results = []

    def get_function(self, target: str) -> str:
        """Sets the type of function to be used in conjunction with the search_folder function"""
        if "--all-folders" == target:
            function = 'all_folders'
        elif '--all-files' == target:
            function = 'all_files'
        else:
            function = 'file_search'
        return function

    def sterilize(self, ster_str: str) -> str:
        """Easy Normalizer for all inputs and outputs of the FileSearcher script"""
        # Replacing all spaces and extra underscores with only underscores
        str_obj = ster_str.replace(" ", "_")
        str_obj = re.sub(" +", " ", str_obj)
        str_obj = re.sub("_+", "_", str_obj)
        str_obj = re.sub("/+", "/", str_obj)
        return str_obj.lower()  # Final Normalization

    def check_parents(self, folders: list) -> None:
        """Sets the first iteration folder list for the program"""
        if self.inputs[0] in folders:
            self.inputs[0] = ''
        # Setting Parent Folders List Using Custom Data-type
        self.folders = list(map(lambda x: self.DataMaker.make_folder_path(
            f'{settings.ROOT_DIR}/{x}', file_path=self.inputs[3]), folders))
        self.folders = list(map(lambda x: self.DataMaker.make_folder_path(
            f'{settings.ROOT_DIR}/{x}', file_path=self.inputs[3]), folders))
        for parent in self.folders:
            # Path Normalization
            sterilized_search = self.sterilize(parent.folder)
            if self.inputs[0] == sterilized_search:
                self.results.append(parent)
            else:
                pass

    def trim(self, item_list: list, mode: str = 'folders') -> list:
        """Gets valid folders out of a list passed into the function"""
        if mode != 'folders':
            temp_files = [file.name for file in item_list if '.' in file.name and not file.name.startswith('.')]
            return temp_files
        self.ignore_folders = ['Public', 'opt', 'Library', 'Pictures', 'Music', 'Sites']
        # List comprehension for getting all folders not in the ignore list
        temp_folds = [
            folder.name for folder in item_list if '.' not in folder.name and folder.name not in self.ignore_folders]
        return temp_folds

    def check_with_result(self, object: str, target: str) -> bool:
        if self.sterilize(object) == self.sterilize(target):
            return True
        else:
            return False

    def change_for_results(self, object: NexusFolderPathObject, result_name: str):
        object.path = os.path.join(object.path, result_name)
        object.folder = result_name
        return object

    def search_folder(self) -> list:
        """Searches Folder location on the computer files and returns complete details"""
        self.folders = os.scandir(
            f'{settings.ROOT_DIR}/')  # Root Directory Scan
        self.folders = self.convert_scan(self.folders, 'folders') # Folder Extraction
        # Checking Parent Exceptions
        self.check_parents(self.folders)
        while self.control != True:
            try:
                for parent_dir in self.folders:
                    subdirectories = os.scandir(f'{parent_dir.path}/')
                    subdirectories = self.convert_scan(subdirectories, 'folders')
                    for sub_directory in subdirectories:
                        sterilized_search = self.sterilize(sub_directory)
                        if self.check_with_result(self.inputs[0], sterilized_search):
                            # Result Formatting Function
                            each_folder_changed = self.change_for_results(parent_dir, sub_directory)
                            self.results.append(each_folder_changed)
                        self.sub_folders.append(self.DataMaker.make_folder_path(
                            f'{parent_dir.path}/{sub_directory}', file_path=self.inputs[3]))
                self.folders = self.sub_folders  # Setting up for next iteration
                self.sub_folders = []  # Resetting the Sub folders list for easy transition
            except Exception:
                pass
                self.control = True
        return self.results

    def convert_scan(self, scanned: list, trimmer = 'files') -> list:
        if trimmer == 'files':
            trimmed = self.trim(scanned, 'files')
            return trimmed
        elif trimmer == 'folders':
            scanned = self.trim(scanned, 'folders')
            return scanned
        else:
            scanned = [item.name for item in scanned if not item.name.startswith('.')]
            return scanned
    
    def global_search(self) -> tuple:
        item_names = []
        item_objects = []
        target = self.inputs[1]
        paths = [object.path for object in self.results]
        for path in paths:
            items = self.convert_scan(list(os.scandir(path)), 'all')
            for item in items:
                if target in self.sterilize(item):
                    item_names.append(item)
                    item_objects.append(self.DataMaker.make_folder_path(
                        f'{path}/{item}', file_path=self.inputs[3]))
        return item_names, item_objects
    
    def all(self, mode='files') -> tuple:
        item_objects = []
        item_names = []
        paths = [object.path for object in self.results]
        for path in paths:
            if mode == 'files':
                items = self.convert_scan(list(os.scandir(path)))
            else:
                items = self.convert_scan(list(os.scandir(path)), 'folders') 
            for item in items:
                item_names.append(item)
                item_objects.append(self.DataMaker.make_folder_path(f'{path}/{item}', file_path=self.inputs[3]))
        return item_names, item_objects
    
    def search(self):
        results = self.search_folder()
        if self.inputs[2] == 'folder':
            if self.record_time == True:
                final_time = time.time() - self.start
                return results, final_time
            return results
        elif self.function == 'all_files':
            (files, objects) = self.all()
        elif self.function == 'all_folders':
            (files, objects) = self.all(mode='folders')
        else:
            (files, objects) = self.global_search()
        
        if self.record_time == True:
            final_time = time.time() - self.start
            return files, objects, final_time
        return files, objects


if __name__ == '__main__':
    folder, target = get_shell_input(1, argv, exceptions=[''])
    if target == '':
        mode = 'folder'
    else:
        mode = ''
    if mode == '':
        search_instance = FileSearcher(folder, target, record_time=True)
        files, objects, final_time = search_instance.search()
        print("FILES:", files, '\n')

        print('OBJECTS:', objects, '\n')
        print("TIME:", final_time)
    else:
        search_instance = FileSearcher(folder, mode=mode, record_time=True)
        folders, final_time = search_instance.search()
        print("FOLDER OBJECT:", folders)
        print("TIME:", final_time)
