# Binary Tree
# ---- construction tree
# ---- pre-order traversal
# ---- middle-order traversal
# ---- post-order traversal
# ---- Broad-First-Search
# ---- Deep-First-Search


class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root_value):

        self.root = Node(root_value)
        self.serial_nodes = list()
        self.serial_nodes.append(self.root)
        self.travel_list = list()
        self.temp_list = list()
        print('init the root node with:', root_value)

    def add_leaf(self, leaf_value):
        print('add the element: ', leaf_value)
        if not self.serial_nodes[0].left:
            self.serial_nodes[0].left = Node(leaf_value)
            self.serial_nodes.append(self.serial_nodes[0].left)
        else:
            self.serial_nodes[0].right = Node(leaf_value)
            self.serial_nodes.append(self.serial_nodes[0].right)
            self.serial_nodes.pop(0)

    def root_prior_traversal(self, node):
        # pre-order traversal
        self.travel_list.append(node)
        if node.left:
            self.root_prior_traversal(node.left)
        if node.right:
            self.root_prior_traversal(node.right)

    def root_middle_traversal(self, node):
        # middle-order traversal
        if node.left:
            self.root_middle_traversal(node.left)
        else:
            return self.travel_list.append(node)
        self.travel_list.append(node)
        if node.right:
            self.root_middle_traversal(node.right)

    def root_last_traversal(self, node):
        # post-order traversal
        if node.left:
            self.root_last_traversal(node.left)
        else:
            return self.travel_list.append(node)
        if node.right:
            self.root_last_traversal(node.right)
        self.travel_list.append(node)

    def broad_first_search(self, node):
        # BFS
        if not self.temp_list:
            # if the node is the root node
            self.temp_list.append(node)
        if node.left and node.right:
            self.temp_list += [node.left, node.right]
            self.broad_first_search(node.left)
            self.broad_first_search(node.right)

    def deep_first_search(self, node):
        # DFS - same as pre-order traversal
        self.root_prior_traversal(node)


if __name__ == '__main__':

    t = BinaryTree(1)
    for i in range(2, 8):
        t.add_leaf(i)

    # pre-order traversal
    print('pre-order traversal')
    t.root_prior_traversal(t.root)
    for i in t.travel_list:
        print(i.value)
    t.travel_list.clear()

    print('middle-order traversal')
    # middle-order traversal
    t.root_middle_traversal(t.root)
    for i in t.travel_list:
        print(i.value)
    t.travel_list.clear()

    print('post-order traversal')
    # post-order traversal
    t.root_last_traversal(t.root)
    for i in t.travel_list:
        print(i.value)

    print('BFS')
    # BFS
    t.broad_first_search(t.root)
    for i in t.temp_list:
        print(i.value)

    print('DFS')
    # DFS
    t.deep_first_search(t.root)
    for i in t.temp_list:
        print(i.value)

















