from curses.ascii import BS
from itertools import cycle
from logging import NullHandler

from sqlalchemy import delete


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
        # Get root node and parent node
        temp = self.root
        parent_node = None

        while temp != None:
            if value <= temp.value:
                if value == temp.value:
                    return temp
                parent_node = temp
                temp = temp.left
            elif value > temp.value:
                parent_node = temp
                temp = temp.right
        return Node(None)

    def remove(self, value):
        if self.root == None:
            return False
        current_node = self.root
        parent_node = None

        while current_node != None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            elif current_node.value == value:
                # Option 1 No right child:
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                # Option 2 Right child which doesnt have a left child
                elif current_node.right.left == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left

                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                # Option 3: Right child that has a left child
                else:
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left != None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent_node == None:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost

                return True


def print_inorder(Node):
    if Node == None:
        return
    print_inorder(Node.left)
    print(Node.value)
    print_inorder(Node.right)


if __name__ == '__main__':
    BST = BinarySearchTree()
    BST.insert(60)
    BST.insert(72)
    BST.insert(30)
    BST.insert(1)
    BST.insert(55)
    BST.insert(38)
    BST.insert(44)
    print_inorder(BST.root)
    print("\n")
    BST.remove(30)
    print_inorder(BST.root)