# Finding least common ancestor



## Testing solution
Run tests:

    python -m unittest tests



## Algorithm Complexity




####Worst case

In a worst case tree may be tall and have two subtrees with N and M nodes

             root
             /  \
            n1  m1
            |   |
            n2  m2
            |   |
            n3  m3
            ... ...
            nN  mN
            ... ...
                mM
                ...


nN and mM - two nodes, N and M - heights of each subtree

- function ``_get_values_path`` returns a path from the node to root.
In worst case the nodes are bottom nodes and finding the path will occure N operations for the left subtree and M operations in right subtree

- function ``_first_value_intersect`` has nested loop, in the worst case the ROOT is a common ancestor, so there will be N * M iterations to find common item in two arrays

Complexity is O(M + N + N * M) which is close to O(N * M)

If a the tree were self-balanced search tree, than the height can be found like:
    N = M = log2 n, where n - amount of nodes in tree
so complexity for this case will be O(2 * log2 n + log2 n * log2 n) which is close to O((log2 n) ^ 2)


####Best case

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




##Memory usage

- The Node instance object is used to store value and a pointer to parent node. There is no collection to store nodes. So it can be said, that all of the memory used by nodes is a memory of pointers to parents and memory of int values. 

Approximately, for n nodes it will use n \* (intSize + pointerSize) = n \* (24 + 24) = 48 \* n (bytes)

- function ``_get_values_path`` implements list concatenation, so there is a new list creation during each recursive call. But old lists (which participate in concatenation) will not be used in next steps, so GC will collect them and delete. At the end of recursive call there be the list L with N items (N - height of the tree). I calculate memory usage of list:

    size = \_size + overhead + garbage_collector + malloc + list-over-allocation


   - \_size = 4 * len (L) = 4N, cause list contains int variables,
   - overhead = 12, cause its a variable (not fixed) type,
   - garabage_collector = 8,
   - malloc = 8,
   - list-over-allocation = 0, cause there is not appending in L,

So, according to this, the size of L array will be = 4N + 12 + 8 + 8 + 0 = 4N + 28 (byes), N - is a height of tree
Function calls twice, there will be two lists L, memory used = 2 *(4N + 28) = 8N + 56

The sys.getsizeof(L) on 64bit Ubuntu, python2.7, shows that the real size of L will be greather about 2 times. So it may be depends on overhead of memory allocated from the
operating system

Result of estimation:

1. Memory to store n nodes in scope: 48 * n (bytes), n - amount of nodes
1. Memory to operate (creating two lists): 8N + 56 (bytes), N - height of tree

If a tree of nodes will be a self-balanced search tree: N = log2 n, and total memory: 48 * n + 8log2 n + 56

*Ex.:*

- for tall tree with height = 10 and 10 nodes: ~600 bytes
- for self-balanced search tree with 10 nodes: ~550 bytes 

