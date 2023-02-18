from tracker import track

def created(event):
    print("lp ", event)
track("/Users/abhijitrawool/Documents/Print", created_func=created)