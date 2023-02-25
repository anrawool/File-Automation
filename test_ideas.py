# FIle for experimentation
import os
import re
from data import *

def path_sterilize(object):
    folder, file, ext = [object.folder, object.file, object.ext]
    folder = re.sub('_+', ' ', folder)
    return folder

maker = DataMaker()
input_obj = maker.make_folder_path(path='Sarthak_Abc')
obj = path_sterilize(input_obj)
print(obj)