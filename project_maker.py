import os
from github import Github
import sys
import json

project_name = sys.argv[1]


class Project_Maker():

    def __init__(self, project_name):
        self.project_name = project_name

    def github_login(self):
        Github_Token = "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"
        github = Github(Github_Token)
        user = github.get_user('anrawool')
        print("Logged into Github Account")
        authed = github.get_user()
        print("Verification Completed")
        return authed

    def make_base(self, project_name):
        try:
            os.mkdir(f"/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")
            self.repo_name = input("Github Repository: ")
            print(f"Making {project_name}...")
        except Exception as e:
            os.system(f"code /Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")
            print(f"Opening {project_name}")
            exit()

        os.chdir(f"/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")
        os.system("touch main.py")
        os.system("touch folder_details.json")
        os.system("touch ReadMe.md")

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
        details = {
            "repo_name":self.repo_name,
            "project_name":project_name,
            "github_repo":repo_exists
        }
        return details
    
    def make(self):
        self.make_base(self.project_name)
        authed = self.github_login()
        repo_exists = self.make_repo(authed)
        details = self.create_details(repo_exists, project_name)
        return details


creater = Project_Maker(project_name)
details = creater.make()

with open("folder_details.json", "w") as outfile:
    json.dump(details, outfile)
os.system(f"code /Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{project_name}")

