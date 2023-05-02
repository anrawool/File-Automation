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
        self.head = self.get_head()
        self.pull_details = self.create_pull_request("Merge Script In Development", "This is a test to check if merge script is up and running...")
        self.merge_branches(self.pull_details[2])
    
    def create_pull_request(self, title, body=''):
        base = self.repo_obj.get_branch(self.merge_to_branch).name
        self.repo_obj.create_pull(title=title, body=body, head=self.head, base=base)
        return self.head, base, title, body

    def get_head(self) -> str:
        if self.merge_branch == 'head':
            command_out = os.popen('git branch').read()
            results = command_out.split('\n')
            for result in results:
                if "*" in result:
                    self.merge_branch = result.replace("* ", "")
                    return self.merge_branch
                else:
                    pass

    def merge_branches(self, title):
        base = self.repo_obj.get_branch(self.merge_to_branch).name
        head = self.repo_obj.get_branch(self.merge_branch)
        print(base)
        print(head)
        merge_to_master = self.repo_obj.merge(base, head.commit.sha, title + ' [Merge] ')
        print(merge_to_master)

RepoMerger(repo_name, merge_branch, merge_to_branch)
