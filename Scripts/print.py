import __meta
import os 
from Controllers.tracker import track
from Controllers.data import *
import re
from settings import ROOT_DIR

"""
Printer terminal commands:

1. lpq: Shows the Printing Queue
2. lprm: Removes a print job from queue
3. lpr: creates a new job in printing queue
4. lpstat -p: Give status of default printer
5. lpstat -t: Gives long status of all printers

"""

class Printer:
    def __init__(self):
        self.compatible = ['.pdf', '.jpeg', '.jpg', '.png', '.txt', '.pages']
        self.compatible_file = False
    def file_name_change(self, object):
        path, file, ext = [object.path, object.file, object.ext]
        # Checking if Path is valid or Ghost
        for extension in self.compatible:
            if extension in ext:
                self.compatible_file = True
                pass

        os.chdir(path)
        temp_file = file.replace(ext, "")
        temp_file = temp_file.replace(".", "_")
        temp_file = temp_file + ext
        final_file = temp_file.replace(" ", '_')
        final_file = re.sub("_+", "_", final_file)
        os.rename(file + ext, final_file)
        return final_file

    def created(self, event):
        datamaker = DataMaker()
        path_obj = datamaker.make_path(path=event.src_path, file_path=False)
        # Checking if Printer is working
        try:
            final_file = self.file_name_change(path_obj)
            # Making Path Compatible For Printing
            os.chdir(f"{ROOT_DIR}/Documents/Sarthak/Print/")
            if self.compatible_file == True:
                os.system(f"lpr {final_file}")
                print("Added to Print Queue")
                # print("Added to Printing Queue")
            else:
                # print("This File Is Incompatible")
                self.compatible_file = False
        except Exception as e:
            # print("The Printer May Be Offline...")
            # print(e)
            pass

printer = Printer()
track(f"{ROOT_DIR}/Documents/Sarthak/Print", created_func=printer.created)
