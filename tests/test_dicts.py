from utils import dicts

def test_get():
    assert dicts.get_val({1:"cat"}, 1, "git") == "cat"
    assert dicts.get_val({}, None, "git") == "git"
    assert dicts.get_val({1:"cat"}, None, "git") == "git"