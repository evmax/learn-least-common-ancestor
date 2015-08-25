Finding least common ancestor
=============================

Test solution
-------------
run tests: python -m unittest tests


Algorithm Complexity
--------------------

*Worst case*

In a worst case tree may be tall and have two subtrees with N and M nodes

             root
             /  \
            n1  m1
            |   |
            n2  m2
            |   |
            n3  m3
            ... ...
            nN
            ... mN
                ...
                mM
                ...


nN and mM - two nodes
N and M - heights of each subtree

- function ``_get_values_path`` returns a path from the node to root.
In worst case the nodes are bottom nodes and finding the path will occure N operations for the left subtree and M operations in right subtree

- function ``_first_value_intersect`` has nested loop, in the worst case the ROOT is a common ancestor, so there will be N * M iterations to find common item in two arrays

Complexity is O(M + N + N*M) which is close to O(N*M)

If a the tree were self-balanced search tree, than the height can be found like:
    N = M = log2 n, where n - amount of nodes in tree
so complexity for this case will be O(2 * log2 n + log2 n * log2 n) which is close to O((log2 n) ^ 2)


*Best case*

             root
             /  \
            n1  ...
            |
            n2
            |
            n3
            ...
            nN
            nN+1
            ...

nN and nN+1 are two nodes.

In a best case, first node is a direct ancestor (parent) of the second node.
- function ``_get_values_path`` will occure 2N + 1 operations (N - height of the first node)
- function ``_first_value_intersect`` will occure only 2 loop operations, because nodes are close to each other.
Complexity is O(2N + 3) which is close to O(N)

If a the tree were self-balanced search tree, than the height can be found like:
    N = log2 n, where n - amount of nodes in tree
so complexity for this case will be O(log2 n)



Memory requirements
-------------------