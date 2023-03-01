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
    def make_path(self, path, file='auto', ext='auto', file_path=True):
        # Formatting
        if file == 'auto':
            remove = os.path.dirname(path)
            file = path.replace(f"{remove}/", "")
        if not file_path:
            path = path.replace(file, "")
        if ext == 'auto':
            auto_ext = os.path.splitext(file)
            ext = auto_ext[1]
            file = file.replace(auto_ext[1], "")
        
        object = NexusPathObject(path=path, file=file, ext=ext)
        return object
    
    def make_folder_path(self, path, folder='auto', ext='auto', file='auto', file_path=True):
        if file == 'auto':
            if "." in path:
                path_replace = os.path.dirname(path)
                file = path.replace(f'{path_replace}/', "")
            else:
                file = None
                ext = None
        if file_path == False:
            path = path.replace(f"{'/'+file}", "")
        if folder == 'auto':
            remove= os.path.dirname(path)
            folder = path.replace(f"{remove}/", "")
            if "." in folder:
                folder = path.replace(f'/{folder}', "")
                folder = folder.replace(f'{os.path.dirname(folder)}/', "")
        else:
            folder = folder
        if ext == 'auto':
            if file != None:
                ext = os.path.splitext(file)[1]
                file = file.replace(ext, "")
        self.fold_path = path
        fold_object = NexusFolderPathObject(path=self.fold_path,  folder=folder, file=file, ext=ext)
        return fold_object


# Example Instance
# datamaker = DataMaker()
# object = datamaker.make_path(path='/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/data.py', path_file=False)