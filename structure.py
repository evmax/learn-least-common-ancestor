# -*- coding: utf-8 -*-
class Node(object):

    """Node of the tree / heap."""

    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
