# tree.py

# Constructor
def tree(value, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [value] + list(branches)

# Selector
def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 1
    else:
        return 1 + max(map(height, branches(t)))

def square_tree(t):
    """Return a tree with the square of every element in t"""
    if is_leaf(t):
        t = tree(t[0]**2)
    else:
        t = tree(t[0]**2, [square_tree(t) for t in branches(t)])
    return t

def tree_size(t):
    """Return the size of a tree."""
    if is_leaf(t):
        return 1
    else:
        return 1 + sum(map(tree_size, branches(t)))

def tree_max(t):
    """Return the max of a tree."""
    if is_leaf(t):
        return t[0]
    else:
        return max(t[0], max(map(tree_max, branches(t))))

def find_path(tree, x):
    """
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    """
    if tree[0] == x:
        return [x]
    elif not is_leaf(tree):
        subpaths = list(map(find_path, branches(tree), [x]*len(branches(tree))))
        # import pdb; pdb.set_trace()
        noneempty_subpath = list(filter(lambda x: x is not None, subpaths))
        if len(noneempty_subpath) <= 0:
            return None
        else:
            return [tree[0]] + noneempty_subpath[0]
    else:
        return None

def hailstone_tree(n, h):
    """
    Generates a tree of hailstone numbers that will
    reach N, with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if h == 0:
        return tree(n)
    else:
        if (n-1) % 3 == 0 and n > 1:
            return tree(n, [hailstone_tree(2 * n, h - 1), hailstone_tree((n - 1) // 3, h - 1)])
        else:
            return tree(n, [hailstone_tree(2 * n, h - 1)])


if __name__ == "__main__":
    t = tree(1,[tree(3,[tree(4),tree(5),tree(6)]), tree(2)])
    t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    t_square = square_tree(t)
    print(t)
    print(t_square)
    print(height(t_square))
    print(tree_size(t_square))
    print(tree_max(t))

    print(find_path(t, 6))

    t = hailstone_tree(1, 4)
    print(t)
