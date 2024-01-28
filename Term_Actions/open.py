import os
import sys
import __meta
from search import *
from sys import argv
from settings import get_shell_input


class Opener:
    def __init__(self, folder, target=None, mode=None) -> None:
        self.folder = folder
        self.target = target
        self.mode = mode
        if self.mode == "folder":
            self.open_folders()
        else:
            self.open_files()

    def ignore_spaces(self, string: str) -> str:
        return string.replace(" ", "\ ")

    def open_files(self):
        search_object = FileSearcher(
            folder=self.folder, target=f"{target}", file_path=False
        )
        (_, file_objects) = search_object.search()
        if len(file_objects) == 0:
            print("No such files found...")
            exit()
        try:
            for file_object in file_objects:
                os.chdir(f"{file_object.path}")
                os.system(
                    f"open {self.ignore_spaces(file_object.file + file_object.ext)}"
                )
        except TypeError:
            for folder in file_objects:
                os.system(f"open {self.ignore_spaces(folder.path)}")

    def open_folders(self):
        search_object = FileSearcher(
            folder=self.folder, mode=self.mode, file_path=False
        )
        folder_objects = search_object.search()
        for folder in folder_objects:
            os.system(f"open {self.ignore_spaces(folder.path)}")


if __name__ == "__main__":
    folder, target = get_shell_input(1, argv, [""])
    if target == "":
        Opener(folder=folder, mode="folder")
        mode = "folder"
    else:
        Opener(folder=folder, target=target)
