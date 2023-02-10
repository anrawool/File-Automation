import os 
from sys import argv

folder = argv[1]
target = argv[2]

class FileSearch():
    def __init__(self, target, folder):
        self.target = target.lower()
        self.folder = folder
        if "." in  self.target:
            self.func = "ext"
        else:
            self.func = "name"
        self.match = False
    
    def name(self):
        final_files_name = []
        folder_loc = self.folder_finder()
        folder_files = os.scandir(f"/Users/abhijitrawool/{folder_loc}")
        for i in folder_files:
            if self.target in i.name.lower():
                print(f"Target Found: {i.name}")
                final_files_name.append(i.name)
        return final_files_name
    
    def ext(self):
        final_files_ext = []
        folder_loc = self.folder_finder()
        folder_files = os.scandir(f"/Users/abhijitrawool/{folder_loc}")
        for i in folder_files:
            if i.name.endswith(target):
                print(f"Target Found: {i.name}")
                final_files_ext.append(i.name)
        
        return final_files_ext
    
    def folder_iterate(self):
        self.folders = ['Documents', 'Downloads']
        for i in self.folders:
            if self.target in i.lower():
                self.match = True
                print(f"Match Found: {i}")
                # break
            else:
                self.match = False
        if self.match == True:
            return self.match
        self.sub_folders = []
        self.dynamic_path = "Users/abhijitrawool"
        self.path_folders = [] # TODO: Used to store paths
        self.counter = 0
        while self.match != True:
            for i in self.folders:
                sub_dir = os.scandir(f"/{self.dynamic_path}/{i}")
                for folder in sub_dir:
                    if not "." in folder.name.lower():
                        if not self.target in folder.name.lower():
                            self.sub_folders.append(folder.name)
                        else:
                            print("Match Found:", folder.name)
                            print("In Folder:", i)
                            self.match = True
                            break
                    if self.match == True:
                        break
                self.counter+=1
                if self.match == True:
                        break
                if self.counter >= len(self.folders):
                    self.folders.clear()
                    for i in self.sub_folders:
                        self.folders.append(i)
                    self.sub_folders.clear()
                    print("Sub Folders:", self.sub_folders)
                    print("Folders:", self.folders)
                    exit()

    def folder_finder(self):
        while self.match != True:
            folder_loc = self.folder_iterate()
        return folder_loc

    def search(self):
        if self.func == "ext":
            files = self.ext()
        else:
            files = self.name()
        return files

search_method = FileSearch(folder, target)
search_method.folder_finder()