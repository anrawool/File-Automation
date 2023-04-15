import os
from github import Github
import sys
import json
from info import Github_Token
from search import *
from settings import *

class Project_Maker():
    def __init__(self, project_name, token, repo='', mode='yes_repo'):
        self.project_name = project_name
        self.mode = mode
        self.repo_name = repo
        self.Github_Token = token
    def github_login(self):
            github = Github(self.Github_Token)
            user = github.get_user('anrawool')
            print("Logged into Github Account")
            authed = github.get_user()
            print("Verification Completed")
            return authed

    def make_base(self, project_name):
        try:
            # print("Project Loc not Available...")
            os.mkdir(f"{ROOT_DIR}/Documents/Sarthak/Programming_Projects/{project_name}")
            print(f"Making {project_name}...")
        except Exception:
            os.system(f"code {ROOT_DIR}/Documents/Sarthak/Programming_Projects/{project_name}")
            print(f"Opening {project_name}")
            exit()

        os.chdir(f"{ROOT_DIR}/Documents/Sarthak/Programming_Projects/{project_name}")
        os.system("touch main.py")
        os.system("touch folder_details.json")
        os.system("touch README.md")
    def make_repo(self, authed):
        if self.repo_name != "":
            os.system("git init")
            os.system("git add .")
            os.system("git commit -m \"Initial Commit\"")
            repo = authed.create_repo(self.repo_name)
            os.system(f"git remote add origin https://github.com/anrawool/{self.repo_name}.git")
            os.system("git push -u origin master")
            print("Github Rpeository Created and Setup")
            repo_exists = "true"
            return repo_exists
        else:
            repo_exists = "false"
            return repo_exists

    @staticmethod
    def create_details(repo_name, repo_exists, project_name):
        details = {
            "repo_name":repo_name,
            "project_name":project_name,
            "github_repo":repo_exists
        }
        return details
    
    def make(self):
        self.make_base(self.project_name)
        if self.mode == "yes_repo":
            authed = self.github_login()
            repo_exists = self.make_repo(authed)
            details = self.create_details(repo_name = self.repo_name, repo_exists=repo_exists, project_name=project_name)
        else:
            details = self.create_details(repo_name = self.repo_name, repo_exists=False, project_name=project_name)
            pass
        with open("folder_details.json", "w") as outfile:
            json.dump(details, outfile)
        os.system(f"code {ROOT_DIR}/Documents/Sarthak/Programming_Projects/{self.project_name}")
        return details

project_name, repo = get_shell_input(1, sys.argv, [None, ])
if repo == None:
    mode = 'no_repo'
else:
    mode = 'yes_repo'

def MakeProject():
    creater = Project_Maker(project_name, Github_Token, repo, mode)
    details = creater.make()
    return details
MakeProject()