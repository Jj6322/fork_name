import os.path
import pytest

def test_push():
    strToFind=" Now the file has more content!"
    assert os.path.exists('./new_file.txt')
    with open('./README.txt', "r") as f:
        assert strToFind in f.read()
