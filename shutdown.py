import os

final = input("Are you sure [Y/n]: ")

if final != "Y":
    exit()
else:
    os.system("sudo shutdown -h now")


