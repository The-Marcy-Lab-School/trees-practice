from practice import binary_tree, get_root_val, insert_left
from typing import List

def test_binary_tree():
    t: List = binary_tree('A')
    assert t[0] == 'A'
    assert t[1] == []
    assert t[2] == []

def test_get_root_val():
    t: List = binary_tree('A')
    assert get_root_val(t) == 'A' 

def test_insert_left():
    t: List = binary_tree('A')
    insert_left(t, 'B')
    assert t[1][0] == 'B'
    insert_left(t, 'Z')
    assert t[1][1][0] == 'B'
    assert t[1][0] == 'Z'


