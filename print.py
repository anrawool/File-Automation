from tracker import track
import os

def sterilize(path):
    os.chdir("/Users/abhijitrawool/Documents/Print/")
    ext = os.path.splitext(path)
    temp_path = path.replace(ext[1], "")
    new_path = temp_path.replace(".", "_")
    final_path = new_path + ext[1]
    final_path = final_path.replace(" ", '_')
    rename_path = temp_path+ext[1]
    os.rename(rename_path, final_path)
    return final_path
def created(event):
    try:
        path = sterilize(event.src_path)
        final = path.replace("/Users/abhijitrawool/Documents/Print/", "")
        os.chdir("/Users/abhijitrawool/Documents/Print/")
        os.system(f"lpr {final}")
    except Exception as e:
        print("The Printer May Be Offline...")
        print(e)
track("/Users/abhijitrawool/Documents/Print", created_func=created)