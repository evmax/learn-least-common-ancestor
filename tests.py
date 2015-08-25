# -*- coding: utf-8 -*-
import unittest
from random import randrange

from structure import Node
from api import lca


class CommonAncestorTestCase(unittest.TestCase):

    """Test for correctness of finding common ancestor's value of two nodes."""

    @staticmethod
    def create_node(parent=None):
        """Creating node with random value."""
        return Node(
            # some random value to be unique
            # in real case uniqueness must be supplied by the user
            value=randrange(10000),
            parent=parent
        )

    def setUp(self):
        self.root = self.create_node()

        # first subtree of the root
        self.n1 = self.create_node(self.root)
        self.n11 = self.create_node(self.n1)
        self.n12 = self.create_node(self.n1)
        self.n13 = self.create_node(self.n1)

        # second subtree of the root
        self.n2 = self.create_node(self.root)
        self.n21 = self.create_node(self.n2)
        self.n22 = self.create_node(self.n2)

    def test_n11_n22(self):
        self.assertEqual(lca(self.n11, self.n22), self.root.value)

    def test_n11_n1(self):
        self.assertEqual(lca(self.n11, self.n1), self.n1.value)

    def test_order(self):
        self.assertEqual(lca(self.n11, self.n1), lca(self.n1, self.n11))

    def test_n22_root(self):
        self.assertEqual(lca(self.n22, self.root), self.root.value)
