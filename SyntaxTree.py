# -*-coding:utf-8 -*-
'''
@File    :   SyntaxTree.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Implementacion de un arbol sintactico
'''

from Stack import *
from Node import *
import copy

class SyntaxTree(object):
    def __init__(self, regex, directo = False):
        
        self.postfix = regex
        self.operators = ['|', '.', '*', '?', '+']
        self.alfabeto = list(set([char for char in self.postfix 
                                 if char not in self.operators 
                                 if char != '(' and char != ')']))
        self.pos = 1
        self.directo = directo
        self.raiz = None
        directo
        self.arbol_sintactico()
    
                
    def arbol_sintactico(self):
        
        tree_stack = Stack()
        
        for char in self.postfix:
            if char in self.alfabeto:
                tree_stack.push(Node(char))
            else:
                if char in ['*', '?', '+']:
                    if tree_stack.get_size() > 0:
                        if self.directo and char == '+':
                                
                                a = tree_stack.pop()
                                
                                a_copy = copy.deepcopy(a)
                                
                                kleene = Node('*', right = a_copy)
                                
                                concat = Node('.', right = kleene, left = a)
                                
                                a_copy.parent = kleene
                                kleene.parent = concat
                                a.parent = concat
                                
                                tree_stack.push(concat)
                                
                        else:
                            right = tree_stack.pop()
                        
                            new = Node(char, right = right)
                        
                            right.parent = new
                        
                            tree_stack.push(new)
                            
                    else:
                        exit()
                        
                else:
                    
                    if tree_stack.get_size() > 1:
                        right = tree_stack.pop()
                        left = tree_stack.pop()
                    
                        new = Node(char, right = right, left = left)
                    
                        right.parent = new
                        left.parent = new
                    
                        tree_stack.push(new)
                    else:
                        exit()
        
        self.raiz = tree_stack.pop()
        
    
    def _height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))    
    
    
    def height(self):
        return self._height(self.raiz)
    
    
    def traverse_postorder(self, node, reachable = None, nodes = None, full = False):
        if not node:
            return
        
        if reachable is None:
            reachable = []
            
        if nodes is None:
            nodes = []
            
        self.traverse_postorder(node.left, reachable, nodes)
        self.traverse_postorder(node.right, reachable, nodes)
        
        reachable.append(node.data)
        nodes.append(node)
        
        if node.data in self.alfabeto:
            # define pos
            node.pos = self.pos
            self.pos += 1
            
            # define nullable
            if node.data == 'ε':
                node.nullable = True
            else:
                node.nullable = False
                
            # define first and last pos
            node.firstpos = [node.pos]
            node.lastpos = [node.pos]
            
        else:
            if node.data == '|':
                node.nullable = node.right.nullable or node.left.nullable
                
                node.firstpos = list(set(node.right.firstpos + node.left.firstpos))
                node.lastpos = list(set(node.right.lastpos + node.left.lastpos))
                
            elif node.data == '.':
                node.nullable = node.right.nullable and node.left.nullable
                
                node.firstpos = list(set(node.right.firstpos + node.left.firstpos)) if node.left.nullable else node.left.firstpos
                node.lastpos = list(set(node.right.lastpos + node.left.lastpos)) if node.right.nullable else node.right.lastpos
                
            elif node.data == '*':
                node.nullable = True
                node.firstpos = node.right.firstpos
                node.lastpos = node.right.lastpos
            
            else:
                pass
        
        return nodes if full else reachable 
    
    
    def __str__(self):
        if self.raiz is not None:
            self.print_tree(self.raiz)
            
        return ("")
