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
