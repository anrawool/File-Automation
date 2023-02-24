from dataclasses import dataclass
import os

@dataclass
class NexusPathObject():
    path : str
    file : str
    ext : str

@dataclass
class NexusFolderPathObject(NexusPathObject):
    folder: str

class DataMaker:
    def make_path(self, path, file='auto', ext='auto', path_file=True):
        self.path = path
        # Formatting
        if file == 'auto':
            remove = os.path.dirname(self.path)
            self.file = self.path.replace(f"{remove}/", "")
        if ext == 'auto':
            auto_ext = os.path.splitext(self.file)
            self.ext = auto_ext[1]
        if not path_file:
            self.path = self.path.replace(self.file, "")
        object = NexusPathObject(path=self.path, file=self.file, ext=self.ext)
        return object
    
    def make_folder_path(self, path, folder='auto', ext=None, file=None):
        if folder == 'auto':
            remove= os.path.dirname(path)
            folder = path.replace(f"{remove}/", "")
        else:
            folder = folder
        self.fold_path = path
        fold_object = NexusFolderPathObject(path=self.fold_path,  folder=folder, file=file, ext=ext)
        return fold_object



# Example Instance
# datamaker = DataMaker()
# object = datamaker.make_path(path='/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/data.py', path_file=False)