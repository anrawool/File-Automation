from settings import *
from github import Github
import os
import sys
import json
from info import Github_Token, Github_User

path = os.path.abspath(os.getcwd())
github = Github(Github_Token)
merge_to_branch, repo_name, merge_branch = get_shell_input(0, sys.argv, ['master', '', 'head'])

def get_repository(path):
    os.chdir(path)
    if not os.path.exists('./.folder_details.json'):
        raise Exception('Please enter repository name manually')
    else:
        try:
            with open('.folder_details.json', 'r') as file:
                file = json.load(file)
                if file['repo_name'] != '':
                    return file['repo_name']
                else:
                    print("No repository available...")
                    exit()
        except Exception:
            raise Exception("There are no details available for this folder.")

if repo_name == '':
    repo_name = get_repository(path)
else:
    pass

class RepoMerger:
    def __init__(self, repository, merge_branch = 'head', merge_to_branch = 'master'):
        self.merge_branch = merge_branch
        self.merge_to_branch = merge_to_branch 
        self.repo_obj = github.get_repo(f"{Github_User}/{repository}")
        repo = self.repo_obj.full_name
        self.repo_name = repo.replace(f'{Github_User}/', "")
        self.merge_branches()
    
    def merge_branches(self):
        if self.merge_branch == 'head':
            command_out = os.popen('git branch').read()
            results = command_out.split('\n')
            for result in results:
                if "*" in result:
                    self.merge_branch = result.replace("* ", "")
                    break
                else:
                    pass
        base = self.repo_obj.get_branch(self.merge_to_branch)
        head = self.repo_obj.get_branch(self.merge_branch)
        merge_to_master = self.repo_obj.merge(base, head.commit.sha, "merge to master")
        print(merge_to_master)

RepoMerger(repo_name, merge_branch, merge_to_branch)
