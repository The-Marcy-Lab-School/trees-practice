from typing import List

def binary_tree(root: any) -> List:
    return [root, [], []]

def get_root_val(root: any) -> any:
    return root[0]

def insert_left(root: List, value: any) -> any:
    t: List = root.pop(1)
    if t == []:
        root.insert(1, binary_tree(value))
    else:
        root.insert(1, [value, t, []])

    return root

t: List = binary_tree('A')
insert_left(t, 'B')
insert_left(t, 'Q')
print(t)