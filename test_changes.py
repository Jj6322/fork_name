import os

from github import Github
from git import Repo

import pytest
TOKEN='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'

def test_push():
    g = Github(TOKEN)
    org = g.get_organization("githubtraining")
    repo = org.get_repo("hellogitworld")
    for r in repo.get_forks():
        if r.full_name=='Jj6322/fork_name':
            my_repo = r
            break
    new = my_repo.get_contents("new_file.txt")
    read = my_repo.get_contents("README.txt")
