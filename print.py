from tracker import track
import os
from data import *
import re

class Printer:
    def __init__(self):
        self.incompatible = ['.rtf', '.crdownload', '.docx']
        self.incompatible_file = False
    def sterilize(self, object):
        path, file, ext = [object.path, object.file, object.ext]
        # Checking if Path is valid or Ghost
        for extension in self.incompatible:
            if extension in ext:
                self.incompatible_file = True
                pass
        
        os.chdir(path)
        temp_file = file.replace(ext, "")
        temp_file = temp_file.replace(".", "_")
        temp_file = temp_file + ext
        final_file = temp_file.replace(" ", '_')
        final_file = re.sub("_+", "_", final_file)
        os.rename(file, final_file)
        return final_file

    def created(self, event):
        datamaker = DataMaker()
        path_obj = datamaker.make_path(path=event.src_path, path_file=False)
        # Chekcing if Printer is working
        try:
            final_file = self.sterilize(path_obj)
            # Making Path Compatible For Printing
            os.chdir("/Users/abhijitrawool/Documents/Print/")
            if self.incompatible_file != True:
                os.system(f"lpr {final_file}")
                print("Added to Printing Queue")
            else:
                print("This File Is Incompatible")
                self.incompatible_file = False
        except Exception as e:
            print("The Printer May Be Offline...")
            print(e)

printer = Printer()
track("/Users/abhijitrawool/Documents/Print", created_func=printer.created)