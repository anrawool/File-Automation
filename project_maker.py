import os
from github import Github
import sys
import json
from info import Github_Token
from search import *

class Project_Maker():
    def __init__(self, project_name, token, repo='', mode='yes_repo', project_loc=None):
        self.project_name = project_name
        self.mode = mode
        self.repo_name = repo
        self.Github_Token = token
        self.project_loc = project_loc
        if self.project_loc != None:
            search_method = FileSearch(folder=self.project_loc, mode='folder', file_path=True)
            folder_obj = search_method.search()
            self.project_loc = folder_obj[0]

    def github_login(self):
            github = Github(self.Github_Token)
            user = github.get_user('anrawool')
            print("Logged into Github Account")
            authed = github.get_user()
            print("Verification Completed")
            return authed

    def make_base(self, project_name, project_loc):
        if self.project_loc == None:
            try:
                print("Project Loc not Available...")
                os.mkdir(f"/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")
                print(f"Making {project_name}...")
            except Exception as e:
                os.system(f"code /Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")
                print(f"Opening {project_name}")
                exit()

            os.chdir(f"/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")
            os.system("touch main.py")
            os.system("touch folder_details.json")
            os.system("touch README.md")
        else:
            try:
                print("Project Loc Availible")
                os.mkdir(f"{self.project_loc.path}")
            except Exception:
                os.system(f"code {self.project_loc.path}")
    def  make_repo(self, authed):
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

    def create_details(self, repo_exists, project_name):
       if self.project_loc != None:
            details = {
                "repo_name":self.repo_name,
                "project_name":project_name,
                "github_repo":repo_exists,
                "path":self.folder_loc.path
            }
       else:
            details = {
                "repo_name":self.repo_name,
                "project_name":project_name,
                "github_repo":repo_exists
            }
       return details
    
    def make(self):
        self.make_base(self.project_name, self.project_loc)
        if self.mode == "yes_repo":
            authed = self.github_login()
            repo_exists = self.make_repo(authed)
            details = self.create_details(repo_exists, project_name)
        else:
            details = self.create_details(repo_exists=False, project_name=project_name)
            pass
        with open("folder_details.json", "w") as outfile:
            json.dump(details, outfile)
        os.system(f"code /Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{self.project_name}")
        return details

class MakeController():
    def __init__(self, mode, folder_loc=None):
        self.mode = mode
        self.folder_loc = folder_loc
        self.run()
    def run(self):
        if self.mode == 'yes_repo':
            if self.folder_loc != '':
                print("controller:", self.folder_loc)
                creater = Project_Maker(project_name, token=Github_Token, repo=github_repo, mode=self.mode, project_loc=self.folder_loc)
            else:
                print(self.folder_loc)
                creater = Project_Maker(project_name, token=Github_Token, repo=github_repo, mode=self.mode)
            details = creater.make()
        else:
            if self.folder_loc != '':
                creater = Project_Maker(project_name, token=Github_Token, repo=None, mode='no_repo', project_loc=self.folder_loc)
            creater = Project_Maker(project_name, token=Github_Token, repo=None, mode='no_repo')
            details = creater.make()
        return details

project_name = sys.argv[1]
try:
    github_repo = sys.argv[2]
    mode = 'yes_repo'
except Exception as e:
    mode = 'no_repo'
try:
    folder = 'Automation'
    folder_loc = folder
    details = MakeController(mode=mode, folder_loc = folder_loc)
except Exception as e:
    print(e)
    exit()
    folder_loc = None
    details = MakeController(mode)
