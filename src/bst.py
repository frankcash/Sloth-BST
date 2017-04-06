from collections import deque

class Node(object):
    """Tree node: left and right child + data which can be any object

    """
    def __init__(self, data):
        """Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Insert new node with data

        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        """Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """Compare 2 trees

        @param node tree to compare
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def print_tree(self):
        """Print tree content inorder

        """
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """Generator to get the tree nodes data

        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

def preorder(node):
    if node is None:
        return None
    else:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is None:
        return None
    else:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def postorder(node):
    if node is None:
        return None
    else:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

def levelorder(head, queue=deque()):
    if head is None:
        return None
    print(head.data)
    [queue.append(node) for node in [head.left, head.right] if node]
    if queue:
        levelorder(queue.popleft(), queue)


def main():
    root = Node(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(7)
    root.insert(14)
    root.insert(13)
    node, parent = root.lookup(14)
    print(node.data)

    print("preorder")
    preorder(root)
    print("inorder")
    inorder(root)
    print("postorder")
    postorder(root)
    print("levelorder")
    levelorder(root)

main()
