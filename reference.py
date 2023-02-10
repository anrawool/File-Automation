import os
from sys import argv

folder = argv[1]
target = argv[2]

class FileSearch():
    def __init__(self, target, folder):
        self.target = target.lower()
        self.folder = folder
        if "." in self.target:
            self.func = "ext"
        else:
            self.func = "name"
    
    def directory_iterate(self, target_folder):
        try:
            os.scandir(f"/Users/abhijitrawool/{target_folder}")
        except Exception:
            print("Folder not found!!")


    def name(self):
        folder_items = os.scandir(f"/Users/abhijitrawool/{self.folder}")
        for i in folder_items:
            if self.target in i.name.lower():
                print(f"Target Found : {i.name}")
    
    def ext(self):
        folder_items = os.scandir(f"/Users/abhijitrawool/{self.folder}")
        for i in folder_items:
            if i.name.endswith(f"{target}"):
                # os.remove(f"../../../../Documents/{i.name}")
                print(f"Target Found: {i.name}")
    def decide_func(self):
        os.system("ls")
        if self.func == "ext":
            self.ext()
        else:
            self.name()
    
    def search(self):
        self.decide_func()

search = FileSearch(target, folder)
search.search()