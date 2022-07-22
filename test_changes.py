import os.path
import pytest

def test_push():
    strToFind="new text"
    assert os.path.exists('./new_file.txt')
    with open('./README.txt', "r") as f:
        assert strToFind in f.read()
