# -*-coding:utf-8 -*-
'''
@File    :   Node.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Implementacion de Nodos para la construccion de Arbol Sintactico
'''

class Node(object):

    def __init__(self, data, parent = None, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        
        self.pos = None
        self.nullable = False
        self.firstpos = []
        self.lastpos = []
        self.followpos = []
        
        