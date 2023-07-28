import os
from dataclasses import dataclass

@dataclass
class NexusPathObject():
    path : str
    file : str
    ext : str

    @property
    def list_return(self):
        return self.path, self.file, self.ext
@dataclass
class NexusFolderPathObject(NexusPathObject):
    folder: str

    @property
    def list_return(self):
        return self.path, self.file, self.ext, self.folder

class DataMaker:
    def make_path(self, path, file='auto', ext='auto', file_path=True):
        # Formatting
        if file == 'auto':
            remove = os.path.dirname(path)
            file = path.replace(f"{remove}/", "")
        else:
            temp_file = path.replace(f"{os.path.dirname(path)}/", "")
            if temp_file != file:
                path = path.replace(temp_file, file)
        if not file_path:
            path = path.replace(file, "")
        if ext == 'auto':
            auto_ext = os.path.splitext(file)
            ext = auto_ext[1]
            file = file.replace(auto_ext[1], "")
        else:
            path_check = path.replace(f'{os.path.dirname(path)}/', "")
            temp_ext = os.path.splitext(path_check)[1]
            if temp_ext != ext:
                path = path.replace(temp_ext, ext)
        if ext == '':
            file = None
            ext = None
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
        if ext == 'auto':
            if file != None:
                ext = os.path.splitext(file)[1]
                file = file.replace(ext, "")
        if file != None:
            if file_path == False:
                path = path.replace(f"{'/'+file+ext}", "")
        else:
            pass
        if folder == 'auto':
            remove= os.path.dirname(path)
            folder = path.replace(f"{remove}/", "")
            if "." in folder:
                folder = path.replace(f'/{folder}', "")
                folder = folder.replace(f'{os.path.dirname(folder)}/', "")
        else:
            folder = folder
        self.fold_path = path
        fold_object = NexusFolderPathObject(path=self.fold_path,  folder=folder, file=file, ext=ext)
        return fold_object
    def change_path(self, object, **change_vals):
        changeable_vals = list(object.__annotations__)
        obj_list_vals = list(object.list_return)
        key_val = zip(changeable_vals, obj_list_vals)
        key_val = dict(key_val)
        for key, val in change_vals.items():
            if key in changeable_vals:
                if key in key_val.keys():
                    key_val[f'{key}'] = val
        if 'path' in change_vals:
            if 'file' in change_vals:
                object = self.make_path(path=key_val['path'], file=key_val['file'])
            else:
                object = self.make_path(path=key_val['path'])
        else:
            object = self.make_path(path=key_val['path'], file=key_val['file'], ext=key['ext'])
        return object

# Example Instance
# datamaker = DataMaker()
# object = datamaker.make_path(path=f'{ROOT_DIR}/Documents/Sarthak/Programming_Projects/Automation')
# object = datamaker.change_path(object=object, path = f'{ROOT_DIR}/Documents/Sarthak/Programming_Projects/Test')
# print(object)
