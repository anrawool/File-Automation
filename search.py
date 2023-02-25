import os 
from sys import argv
from data import *

folder = argv[1]
target = argv[2]

class FileSearch():
    def __init__(self, folder, target):
        self.DataMakerObj = DataMaker()
        self.sub_folders = []
        self.target = target.lower()
        self.target_folder = folder.lower()
        if "." in  self.target:
            self.func = "ext"
        else:
            self.func = "name"
        self.control = False
        self.results = []
        #TODO: Remove Extra results
        # TODO: Fix Undetection due to Double word searches
    
    def name(self):
        final_files_name = []
        folder_loc = self.folder_finder()
        folder_files = os.scandir(f"/Users/abhijitrawool/{folder_loc}")
        for i in folder_files:
            if self.target in i.name.lower():
                # print(f"Target Found: {i.name}")
                final_files_name.append(i.name)
        return final_files_name
    
    def ext(self):
        final_files_ext = []
        folder_loc = self.folder_finder()
        folder_files = os.scandir(f"/Users/abhijitrawool/{folder_loc}")
        for i in folder_files:
            if i.name.endswith(target):
                # print(f"Target Found: {i.name}")
                final_files_ext.append(i.name)
        
        return final_files_ext
    
    def folder_trim(self, fold_list):
        self.temp_folds = []
        self.ignore_folds = ['Public', 'Movies', 'Applications', 'opt', 'Library', 'Desktop', 'Pictures', 'Music', 'Sites']
        for folder in fold_list:
            if not "." in folder.name and not folder.name in self.ignore_folds:
                self.temp_folds.append(folder.name)
            else:
                pass
        return self.temp_folds

    def search_folder(self):
        self.folders = os.scandir("/Users/abhijitrawool/")
        self.folders = [folder for folder in self.folders]
        self.folders = self.folder_trim(self.folders)
        self.folders = [self.DataMakerObj.make_folder_path(path=f'/Users/abhijitrawool/{fold}') for fold in self.folders]
        for fold in self.folders:
            if self.target_folder == fold.folder.lower():
                self.results.append(fold)
            else:
                pass
        while self.control != True:
            try:
                for each_folder in self.folders:
                    dirs = [dir for dir in os.scandir(f"{each_folder.path}/")]
                    dirs = self.folder_trim(dirs)
                    for dir in dirs:
                        if self.target_folder == dir.lower():
                            # print(f"Match Found!!! {each_folder.path}/{dir}")
                            self.results.append(each_folder)
                        self.sub_folders.append(self.DataMakerObj.make_folder_path(path=f'{each_folder.path}/{dir}'))
                self.folders = self.sub_folders
                self.sub_folders = []
            except NotADirectoryError:
                pass
                self.control = True
        return self.results

    def folder_finder(self):
        while self.control != True:
            folder_loc = self.search_folder()
        return folder_loc

    def search(self):
        if self.func == "ext":
            files = self.ext()
        else:
            files = self.name()
        return files

search_method = FileSearch(folder, target)
obj = search_method.folder_finder()
print("Result:", obj)