import os 
from sys import argv
from data import *
import re
import time 

mode = ''
folder = argv[1]
try:
    target = argv[2]
except Exception:
    mode = 'folder'

class FileSearch():
    def __init__(self, folder, target='', mode=None):
        self.mode = mode
        self.DataMakerObj = DataMaker()
        self.sub_folders = []
        self.target = target.lower()
        self.target_folder = self.folder_sterilize(folder)
        if "." in  self.target:
            self.func = "ext"
        elif "_all_folders" == self.target:
            self.func = 'all_folders'
        elif "_all_files" == self.target:
            self.func = 'all_files'
        else:
            self.func = "name"
        self.control = False
        self.results = []
    def folder_sterilize(self, folder):
        folder = re.sub('_+', ' ', folder)
        return folder.lower()
    
    def name(self, folder_loc, folder_obj):
        final_files_name = []
        folder_objs = []
        try:
            folder_files = os.scandir(f'{folder_loc}/{self.target_folder}')
            for i in folder_files:
                if self.target in i.name.lower():
                    folder_obj.file = i.name.replace(os.path.splitext(i.name)[1], '')
                    folder_obj.ext = os.path.splitext(i.name)[1]
                    folder_objs.append(folder_obj)
                    final_files_name.append(i.name)
        except FileNotFoundError:
            pass
        return (final_files_name, folder_objs)
    
    def ext(self, folder_loc, folder_obj):
        final_files_ext = []
        folder_objs = []
        folder_files = os.scandir(f"{folder_loc}/{self.target_folder}")
        try:
            for i in folder_files:
                if i.name.endswith(target):
                    folder_obj.file = i.name.replace(os.path.splitext(i.name)[1], '')
                    folder_obj.ext = os.path.splitext(i.name)[1]
                    # print(f"Target Found: {i.name}")
                    folder_objs.append(folder_obj)
                    final_files_ext.append(i.name)
        except FileNotFoundError:
            pass
        return (final_files_ext, folder_objs)
    
    def folder_trim(self, fold_list):
        self.temp_folds = []
        self.ignore_folds = ['Public', 'Movies', 'Applications', 'opt', 'Library', 'Desktop', 'Pictures', 'Music', 'Sites']
        for folder in fold_list:
            if not "." in folder.name and not folder.name in self.ignore_folds:
                self.temp_folds.append(folder.name)
            else:
                pass
        return self.temp_folds

    def file_trim(self, file_list):
        self.temp_files = []
        for file in file_list:
            if not file.name.startswith('.'):
                if '.' in file.name:
                    self.temp_files.append(file.name)
            else:
                pass
        return self.temp_files


    def search_folder(self):
        self.folders = os.scandir("/Users/abhijitrawool/")
        self.folders = [folder for folder in self.folders]
        self.folders = self.folder_trim(self.folders)
        self.parent_folders = self.folders
        if self.target_folder in self.parent_folders:
            self.target_folder = ''
        self.folders = [self.DataMakerObj.make_folder_path(path=f'/Users/abhijitrawool/{fold}') for fold in self.folders]
        for fold in self.folders:
            search_fold = self.folder_sterilize(fold.folder)
            if self.target_folder == search_fold:
                self.results.append(fold)
            else:
                pass
        while self.control != True:
            try:
                for each_folder in self.folders:
                    dirs = [dir for dir in os.scandir(f"{each_folder.path}/")]
                    dirs = self.folder_trim(dirs)
                    for dir in dirs:
                        search_dir = self.folder_sterilize(dir)
                        if self.target_folder == search_dir:
                            self.results.append(each_folder)
                        self.sub_folders.append(self.DataMakerObj.make_folder_path(path=f'{each_folder.path}/{dir}'))
                self.folders = self.sub_folders
                self.sub_folders = []
            except NotADirectoryError:
                pass
                self.control = True
        return self.results

    def all_folders(self, folder_obj):
        final_folder_objs_all = []
        items = os.scandir(f"{folder_obj.path}/{self.target_folder}")
        final_folders_all = [folder for folder in items]
        final_folders_all = self.folder_trim(final_folders_all)
        for folder in final_folders_all:
            folder = self.folder_sterilize(folder=folder)
            folder_object = self.DataMakerObj.make_folder_path(path=f'{folder_obj.path}/{self.target_folder}/{folder}')
            final_folder_objs_all.append(folder_object)
        return (final_folders_all, final_folder_objs_all)

    def all_files(self, folder_obj):
        final_files_objs_all = []
        items = os.scandir(f"{folder_obj.path}/{self.target_folder}")
        final_files_all = [file for file in items]
        final_files_all = self.file_trim(final_files_all)
        for file in final_files_all:
            folder_object = self.DataMakerObj.make_path(path=f'{folder_obj.path}/{file}')
            final_files_objs_all.append(folder_object)
        return (final_files_all, final_files_objs_all)

    def search(self):
        result_files = []
        result_folder_objs = []
        while self.control != True:
            results = self.search_folder()
        if self.mode == 'folder':
            return results
        for result in results:
            if self.func == 'name':
                (files, folder_obj) = self.name(folder_loc=result.path, folder_obj=result)
                if files != []:
                    result_files.append(files)
                    result_folder_objs.append(folder_obj)
            elif self.func == 'all_folders':
                (files, folder_obj) = self.all_folders(folder_obj=result)
                if files != []:
                    result_files.append(files)
                    result_folder_objs.append(folder_obj)
            elif self.func == 'all_files':
                (files, folder_obj) = self.all_files(folder_obj=result)
                if files != []:
                    result_files.append(files)
                    result_folder_objs.append(folder_obj)
            else:
                (files, folder_obj) = self.ext(folder_loc=result.path, folder_obj=result)
                if files != []:
                    result_files.append(files)
                    result_folder_objs.append(folder_obj)
        return (result_files, result_folder_objs)

if mode != 'folder':
    search_method = FileSearch(folder, target)
    (files_list, folds_list) = search_method.search()
    print("Final Files List:", files_list)
    print("\nFinal Folders List:", folds_list)
else:
    search_method = FileSearch(folder, mode=mode)
    folder_loc = search_method.search()
    print("Folder Location is:", folder_loc)