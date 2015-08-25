# -*- coding: utf-8 -*-
def _get_values_path(node):
    """
    Collecting values of the node's path from node to the root.

    :rtype: list
    """
    start = [node.value, ]
    if node.parent:
        return start + _get_values_path(node.parent)
    else:
        return start


def _first_value_intersect(arr1, arr2):
    """
    Finding first value which present in both colections: ``arr1`` & ``arr2``.

    :param list arr1: first collection
    :param list arr2: second collection
    """
    for v1 in arr1:
        for v2 in arr2:
            if v1 == v2:
                return v1


def lca(node1, node2):
    """
    Closest common ancestor of two nodes.

    ..note::

        Returns None if nodes are in different trees (with different tree root)

    :param node1: first node
    :type node1: structure.Node
    :param node2: second node
    :type node2: structure.Node
    :returns: value of the common ancestor
    """
    node1_path_values = _get_values_path(node1)
    node2_path_values = _get_values_path(node2)

    return _first_value_intersect(node1_path_values, node2_path_values)
