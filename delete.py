from search import FileSearcher
from sys import argv
import os
from settings import get_shell_input
import shutil

in_folder, del_file = get_shell_input(2, argv)
print(in_folder)
search_method = FileSearcher(in_folder, del_file, file_path=False)
del_files, folder_objs = search_method.search()
top_results = folder_objs[0]
print(folder_objs)
for result in top_results:
    print(result.path)
    os.chdir(result.path)
    sure = input(
        f"Are you sure you want to delete {result.file} in {result.folder}? [Y/n]: ")
    try:
        if sure == "Y":
            if '.' in result.path:
                os.remove(f'{result.file+result.ext}')
            else:
                shutil.rmtree(f'{result.folder}')
        else:
            pass
    except Exception as e:
        print(e)
        pass
