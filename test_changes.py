import os

from github import Github
from git import Repo

import pytest


def test_push():
    print('hello')
    repo = Repo(os.getcwd() + "/" + 'os.getcwd()/fork_name')
    commits_ahead = repo.iter_commits(f'{repo.remote()}..{repo.active_branch}')
    assert sum(1 for c in commits_ahead) == 0
