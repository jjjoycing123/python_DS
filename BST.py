from curses.ascii import BS
from logging import NullHandler


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        # Get root node and parent node
        temp = self.root
        parent_node = None
        # iterate through the tree
        while temp != None:
            if value <= temp.value:
                parent_node = temp
                temp = temp.left
            elif value > temp.value:
                parent_node = temp
                temp = temp.right

        if value <= parent_node.value:
            parent_node.left = Node(value)
            return
        parent_node.right = Node(value)

    def lookup(self, value):
        print("poop")


def print_inorder(Node):
    if Node == None:
        return
    print_inorder(Node.left)
    print(Node.value)
    print_inorder(Node.right)


if __name__ == '__main__':
    BST = BinarySearchTree()
    BST.insert(9)
    BST.insert(4)
    BST.insert(6)
    BST.insert(20)
    BST.insert(170)
    BST.insert(15)
    BST.insert(1)

    print_inorder(BST.root)
