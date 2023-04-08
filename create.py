from search import *
import sys
import os
from project_maker import Project_Maker
import json

try:
    in_folder = sys.argv[1]
    new_folder = sys.argv[2]
except Exception:
    exit()
def create(in_folder, new_folder):
    incompat = ['documents', 'downloads']
    search_method = FileSearch(folder=in_folder, mode='folder', file_path=True)
    results = search_method.search()
    top_result_path= results[0].path
    if in_folder.lower() in incompat:
        in_folder = ''
    os.chdir(f"{top_result_path}/{in_folder}")
    os.system(f"mkdir {new_folder}")
    details = Project_Maker.create_details('', False, new_folder)
    os.chdir(new_folder)
    os.system("touch folder_details.json")
    with open("folder_details.json", "w") as outfile:
        json.dump(details, outfile)

create(in_folder, new_folder)