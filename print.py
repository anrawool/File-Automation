from tracker import track
import os
import time
import subprocess

def sterilize(path):
    if path.endswith('.crdownload'):
        print("This is a invalid file")
        os.system("python3 print.py")

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
    cmd = ['lpstat', '-p']
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE ).communicate()[0]
    output = output.decode()
    if "offline" in output:
        print("The Printer Is Not Swtiched On.")
        print("Waiting...")
        time.sleep(60)
        pass
    else:
        pass
    try:
        path = sterilize(event.src_path)
        final = path.replace("/Users/abhijitrawool/Documents/Print/", "")
        os.chdir("/Users/abhijitrawool/Documents/Print/")
        print("Printed")
        os.system(f"lpr {final}")
        print("Printed")
    except Exception:
        print("The Printer May Be Offline...")
track("/Users/abhijitrawool/Documents/Print", created_func=created)