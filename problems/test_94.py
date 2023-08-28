""" Construct a tree"""
from typing import Optional, List


# leet code prompt with a tree node structure
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: Optional[TreeNode]) -> List[int]:
    # python has support for closures
    results = []

    def traverse(node: TreeNode):
        # return early and break out early
        if not node:
            return None

        # visit the left first (in order)
        # this will keep going to the lower depth
        # with value printed
        traverse(node.left)

        # your result now value the value from 1..
        results.append(node.val)

        # You have checked left already and now go to the right
        traverse(node.right)

    traverse(root)
    return results


def test_naive_approach():
    myTree = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    results = in_order_traversal(myTree)
    assert results == [1, 3, 2]
