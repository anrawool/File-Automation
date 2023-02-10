import os
import sys
import json
from github import Github
import shutil

sure = input("Are you sure? [Y/n]: ")
if sure != "Y":
  exit()
else:
  pass

delete_obj = sys.argv[1]

class Delete_Project():

  def __init__(self, project_delete):
    self.project_delete = project_delete
  
  def delete(self):
    try:
      os.chdir(f"/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/{self.project_delete}")
      with open('folder_details.json') as f:
        data = json.load(f)
        repo_name = data['repo_name']
        repo_exists = data['github_repo']
        if repo_exists == 'true':
          # Login
          Github_Token = "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"
          github = Github(Github_Token)
          user = github.get_user('anrawool')
          print("Logged into Github Account")
          authed = github.get_user()
          print("Verification Completed")
          repo = authed.get_repo(repo_name)
          repo.delete()
          print("Repository Deleted")
          os.chdir("/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/")
          shutil.rmtree(f"{self.project_delete}")
          print("Folder Deleted")
        else:
          os.chdir("/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/")
          shutil.rmtree(f"{self.project_delete}")
          print("Folder Deleted")
    except Exception as e:
      print(f"An Problem Has Occured: {e}")

deleter = Delete_Project(delete_obj)
deleter.delete()