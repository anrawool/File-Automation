import os
import sys
path = os.path.join('../')
sys.path.append(path)
import json
from github import Github
import shutil
from settings import ROOT_DIR
from info import Github_Token

sure = input("Are you sure? [Y/n]: ")
if sure != "Y":
    exit()
else:
    pass

delete_obj = sys.argv[1]


class Delete_Project():

    def __init__(self, project_delete, token):
        self.project_delete = project_delete
        self.Github_Token = token

    def delete(self):
        try:
            os.chdir(
                f"{ROOT_DIR}/Documents/{self.project_delete}")
            with open('.folder_details.json') as f:
                data = json.load(f)
                repo_name = data['repo_name']
                repo_exists = data['github_repo']
                if repo_exists == 'true':
                    # Login
                    github = Github(self.Github_Token)
                    user = github.get_user('anrawool')
                    print("Logged into Github Account")
                    authed = github.get_user()
                    print("Verification Completed")
                    repo = authed.get_repo(repo_name)
                    repo.delete()
                    print("Repository Deleted")
                    os.chdir(
                        f"{ROOT_DIR}/Documents/")
                    shutil.rmtree(f"{self.project_delete}")
                    print("Folder Deleted")
                else:
                    os.chdir(
                        f"{ROOT_DIR}/Documents/")
                    shutil.rmtree(f"{self.project_delete}")
                    print("Folder Deleted")
        except Exception as e:
            print(f"An Problem Has Occurred: {e}")


try:
    deleter = Delete_Project(delete_obj, token=Github_Token)
    deleter.delete()
except Exception:
    print("This Folder Does Not Exist")
