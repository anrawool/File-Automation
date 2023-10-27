import __meta
import json
from Controllers import encrypter
from settings import get_shell_input
import os

github_token = input("Please enter your github token: ")
google_token = input("Please enter your google token: ")
email_id = input("Please enter your email id: ")
github_id = input("Please enter your github id: ")

info_code = f"""
import __meta
from Controllers.encrypter import AEA

coderinstance = AEA(key_path='{os.path.abspath('../PvtInfo/')}/important_key.json')
Github_Token = coderinstance.decrypt_file('{os.path.abspath('../PvtInfo/')}/github_token.txt')
Google_Token = coderinstance.decrypt_file('{os.path.abspath('../PvtInfo/')}/google_token.txt')
Github_User= '{github_id}'
Email_Address = '{email_id}'
"""

encrypterObj = encrypter.AEA(save_key=True, key_path='../PvtInfo/important_key.json', write_to_file=True)

encrypted_github_token = encrypterObj.encrypt_text(github_token, file_path='../PvtInfo/github_token.txt')
encrypted_google_token = encrypterObj.encrypt_text(google_token, file_path='../PvtInfo/google_token.txt')

print("Thank you very much, this may take a moment...")

with open("../PvtInfo/info.py", 'w+') as file:
    file.write(info_code)

confirmation_env = input("Would you like to setup a environment for latest stable version? [Y/n]: ")
if confirmation_env.lower() == 'y':
    print("Okay, this may take a moment...")
    os.system("pip install virtualenv")
    os.system("virtualenv ../LatestEnv")
else:
    print("Okay, thank you...")

github_repo = input("Do you have a online github repository you want to connect this folder to? [y/n]: ")
if github_repo.lower() == 'y':
    github_repo_name = input("Please enter then name of your github repository: ")
    with open("../.folder_details.json", "w+") as json_file:
        repo_information = {"repo_name": github_repo_name, "project_name": "Automation", "github_repo": "true"}
        json.dump(repo_information, json_file)
else:
    with open("../.folder_details.json", "w+") as json_file:
        repo_information = {"repo_name": "", "project_name": "Automation", "github_repo": "false"}
        json.dump(repo_information, json_file)
