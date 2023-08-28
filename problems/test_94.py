"""Using primitives construct a tree and traverse
iteratively or recursively"""

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


def out_of_order_traversal(root: Optional[TreeNode]) -> List[int]:
    # python has support for closures
    results = []

    def traverse(node: TreeNode):
        # return early and break out early
        if not node:
            return None

        # visit the right first (in order)
        # this will keep going to the lower depth
        # with value printed
        traverse(node.right)

        # your result now value the value from 1..
        results.append(node.val)

        # You have checked left already and now go to the right
        traverse(node.left)

    traverse(root)
    return results


def post_order_traversal(root: Optional[TreeNode]) -> List[int]:
    # python has support for closures
    results = []

    def traverse(node: TreeNode):
        # return early and break out early
        if not node:
            return None

        # visit children then append the parent of that subtree
        traverse(node.left)

        # You have checked left already and now go to the right
        traverse(node.right)

        # your result now value the value from 1..
        results.append(node.val)

    # this way the root is at the end of the array
    traverse(root)
    return results


def iterative_traversal_in_order(root) -> List[int]:
    """Using an iterative approach
    left root right inorder

    Saves memory ad stack will always have one node
    in its history

    Result array will grow in size and can run out of
    memory

    this is probably better suited for searching rather than
    aggregating results
    """

    # stack is your history and keeps state
    # of the last visited node
    stack = []
    result = []
    current = root

    while stack or current:
        # check if the root node is not null
        if current:
            # root is added to stack here
            stack.append(current)
            # starts at root then goes to the left
            # 1 --> 3
            current = current.left

        else:
            # Now we are at a dead end so we go right
            # from the last visited node
            # which will always be inside the stack[-1]
            current = stack.pop()
            result.append(current.val)
            current = current.right
    return result


def test_naive_approach():
    """Tree looks like:
           root (1)
           /     \
        null     (2)
                /
               (3)
    """
    myTree = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    results = in_order_traversal(myTree)
    assert results == [1, 3, 2]

    results = out_of_order_traversal(myTree)
    assert results == [2, 3, 1]

    results = post_order_traversal(myTree)
    assert results == [3, 2, 1]

    results = iterative_traversal_in_order(myTree)
    assert results == [1, 3, 2]
