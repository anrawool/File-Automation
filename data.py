from dataclasses import dataclass
import os

@dataclass
class NexusPathObject():
    path : str
    file : str
    ext : str

class DataMaker:
    def make_path(self, path, file='auto', ext='auto', path_file=True):
        self.path = path
        # Formatting
        if file == 'auto':
            remove = os.path.dirname(self.path)
            print("remove:", remove)
            self.file = self.path.replace(f"{remove}/", "")
        if ext == 'auto':
            auto_ext = os.path.splitext(self.file)
            print(auto_ext)
            self.ext = auto_ext[1]
        if not path_file:
            self.path = self.path.replace(self.file, "")
        object = NexusPathObject(path=self.path, file=self.file, ext=self.ext)
        return object


# Example Instance
# datamaker = DataMaker()
# object = datamaker.make_path(path='/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/data.py', path_file=False)