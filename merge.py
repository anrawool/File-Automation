from settings import *
from github import Github
import os
from itertools import combinations
import sys
import json
from info import Github_Token, Github_User

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

class RepoMerger:

    def __init__(self, repository, merge_branch = 'head', merge_to_branch = 'master', title = 'Merge to Master', body = '', all = False):
        self.merge_branch = merge_branch
        self.merge_to_branch = merge_to_branch 
        self.repo_obj = github.get_repo(f"{Github_User}/{repository}")
        self.repo_name = self.repo_obj.full_name.replace(f'{Github_User}/', "")
        self.head = self.get_head()
        if all == True:
            self.merge(title, body, True)
        self.merge(title, body)

    
    def create_pull_request(self, title, body='', base = None, head = None):
        if base == None and head == None:
            base = self.repo_obj.get_branch(self.merge_to_branch).name
            self.repo_obj.create_pull(title=title, body=body, head=self.head, base=base)
        elif base != None:
            base = self.repo_obj.get_branch(base).name
            self.repo_obj.create_pull(title=title, body=body, head=self.head, base=base)
        elif head != None:
            base = self.repo_obj.get_branch(self.merge_to_branch).name
            self.repo_obj.create_pull(title=title, body=body, head=head, base=base)
        else:
            base = self.repo_obj.get_branch(base).name
            self.repo_obj.create_pull(title=title, body=body, head=head, base=base)
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
        commit_code = self.repo_obj.merge(base, head.commit.sha, title + ' [Merge] ')
    
    def get_all_branches(self):
        command_result = os.popen('git branch').read()
        results = command_result.split('\n')
        for idx, result in enumerate(results):
            results[idx] = result.replace("*", "").strip()
            if result == '':
                del results[idx]
        return results
    
    def merge(self, title, body, all=False):
        if self.merge_to_branch != 'master':
            title[-1] = self.merge_to_branch
        if all == False:
            self.pull_details = self.create_pull_request(title, body)
            self.merge_branches(self.pull_details[2])
        else:
            all_branches = self.get_all_branches()
            all_combinations  =list(combinations(all_branches, 2))
            for base, head in all_combinations:
                title_words = title.split(' ')
                title_words[-1] = base
                title = ''.join(word + ' ' for idx, word in enumerate(title_words) if idx != -1)
                title = title.strip()
                self.pull_details = self.create_pull_request(title, body, base, head)
                self.merge_branches(self.pull_details[2])

path = os.path.abspath(os.getcwd())
github = Github(Github_Token)
merge_branch, repo_name, merge_to_branch = get_shell_input(0, sys.argv, ['head', '', 'master'])

if repo_name == '':
    repo_name = get_repository(path)
else:
    pass

RepoMerger(repo_name, merge_branch, merge_to_branch, all=True)
