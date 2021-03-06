from unittest import *


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        def traverse(current):
            yield current
            if current.left:
                yield from traverse(current.left)
            if current.right:
                yield from traverse(current.right)

        for node in traverse(self):
            yield node.value


class Evaluate(TestCase):
    def test_exercise(self):
        node = Node("a", Node("b", Node("c"), Node("d")), Node("e"))
        self.assertEqual(
            "abcde", "".join(list(node.traverse_preorder()))
        )
