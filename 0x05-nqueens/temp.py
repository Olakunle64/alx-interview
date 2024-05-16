#!/usr/bin/python3
"""Nqueens Algorithm"""
from typing import List

class Tree():
    """A node with three pointers:
        prev_node: pointer
        right_node: pointer
        left_node: pinter
    """
    def __init__(self, data, parent=None, right_node=None, left_node=None):
        """Initializing"""
        self.parent = parent
        self.right_node = right_node
        self.left_node = left_node
        self.data = data

    @property
    def parent(self):
        """parent getter"""
        return self.__parent

    @parent.setter
    def parent(self, node):
        """parent setter"""
        if isinstance(node, Tree) or node is None:
            self.__parent = node
        else:
            raise TypeError("parent must be a Node object")

    @property
    def right_node(self):
        """right_node getter"""
        return self.__right_node

    @right_node.setter
    def right_node(self, node):
        """right_node setter"""
        if isinstance(node, Tree) or node is None:
            self.__right_node = node
        else:
            raise TypeError("right_node must be a Node object")

    @property
    def left_node(self):
        """left_node getter"""
        return self.__left_node

    @left_node.setter
    def left_node(self, node):
        """right_node setter"""
        if isinstance(node, Tree) or node is None:
            self.__left_node = node
        else:
            raise TypeError("left_node must be a Node object")

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")


class BinaryTree():
    """Binary Tree data structures"""
    def insert_left(self, value, mother):
        """insert a node to the left"""
        if not isinstance(mother, Tree):
            raise TypeError("mother must be of type Tree")
        newTree = Tree(value)
        mother.left_node = newTree
        newTree.parent = mother.parent
        return newTree

    def insert_right(self, value, mother):
        """insert a node to the right"""
        if not isinstance(mother, Tree):
            raise TypeError("mother must be of type Tree")
        newTree = Tree(value)
        mother.right_node = newTree
        newTree.parent = mother.parent
        return newTree

    def printTree(self, mother):
        """print a Tree"""
        if mother is None:
            return
        if not isinstance(mother, Tree):
            raise TypeError("mother must be of type Tree")
        print(mother.data)
        self.printTree(mother.left_node)
        self.printTree(mother.right_node)

# mother = Tree(0)
# worker = BinaryTree()
# left_mother = worker.insert_left(1, mother)
# right_mother = worker.insert_right(2, mother)
# current = left_mother
# left_mother = worker.insert_left(3, left_mother)
# current = worker.insert_right(4, current)
# worker.printTree(mother)

def row_checker(queen1: List, queen2: List) -> bool:
    """Check if the queens are on the same row/rank

        Args:
            queen1: a list
            queen2: a list

        Return: return True if queens are attacking
                eachother on the same row
                otherwise return False.
    """
    if queen1[0] == queen2[0]:
        return True
    else:
        return False

def column_checker(queen1: List, queen2: List) -> bool:
    """Check if the queens are on the same column/file

        Args:
            queen1: a list
            queen2: a list

        Return: return True if queens are attacking
                eachother on the same column
                otherwise return False.
    """
    if len(queen2) < 2 or len(queen1) < 2:
        return False 
    if queen1[1] == queen2[1]:
        return True
    else:
        return False

def diagonal_checker(queen1: List, queen2: List) -> bool:
    """Check if the queens are on the same diagonal

        Args:
            queen1: a list
            queen2: a list

        Return: return True if queens are attacking
                eachother on the same diagonal
                otherwise return False.
    """
    pass

worker = BinaryTree()
chess = [[i] for i in range(4)]

def nQueens(mother) -> List[List[int]]:
    """A program that solves the N queens problem.

        Description: The N queens puzzle is the
                        challenge of placing N non-attacking
                        queens on an N×N chessboard.

        Args:
            n: an integer

        Return: return a list of list
    """
    i = 0
    while True:
        parent = worker.insert_left(1)
        chess[i][i] = i
        if not row_checker(chess[i], chess[i + 1]) and not column_checker(chess[i], chess[i + 1]):
            



nQueens(4)






