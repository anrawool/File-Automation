from tracker import track
import os

def created(event):
    try:
        os.system("lp {event.src_path}")
    except Exception:
        print("The Printer May Be Offline...")
track("/Users/abhijitrawool/Documents/Print", created_func=created)