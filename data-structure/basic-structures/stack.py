"""
Federal University of Pernambuco - UFPE
Informatics Center - CIn
Bachelor of Information Systems 
IF969 - Algorithms and Data Structeres
Professor: Hansenclever Bassani
Author: Pedro Manoel Farias Sena de Lima
Email: pmfsl@cin.ufpe.br

Copyright © 2021 all rights reserved

Description: Implementation of Stack data structure.
"""
from node import Node

class Stack:
    '''
    Stack implementation
    '''
    def __init__(self):
        self.__start = None
    
    def is_empty(self):
        '''
        Return True if stack is empty
        '''
        return self.__start is None
    
    def search(self, value):
        '''
        Return True if a node it is in the stack.
        '''
        if self.is_empty():
            return False
        else:
            node = self.__start
            node_found = False
            while node and not(node_found):
                if node.get_value() == value:
                    no_achado = True
                else:
                    node = node.get_next()
            return node_found
        
    def push(self, value):
        '''
        Insert a node in the stack
        '''
        node = Node(value)
        node.set_next(self.__start)
        self.__start = node
    
    def pop(self):
        '''
        Remove the last node from the stack
        '''
        if self.is_empty():
            raise ValueError('Stack.pop(): empty stack')
        else:
            node = self.__start.get_next()
            self.__start.set_next(None)
            self.__start = node
    
    def __len__(self):
        '''
        Retourn the stack length
        '''
        if self.is_empty():
            return 0
        else:
            count = 0
            node = self.__start

            while node:
                count += 1
                node = node.get_next()
            return count
    
    def __iter__(self):
        '''
        Stack iterator
        '''
        self.__index = int()
        return self
    
    def __next__(self):
        '''
        Return the iterator node
        '''
        if self.__index < self.__len__():
            node = self.__getitem__(self.__index)
            self.__index += 1
            return node
        else:
            raise StopIteration
        
    def __getitem__(self, key):
        '''
        Return the value os a key.
        '''
        index = self.__len__()-1
        if (key > index) or (self.is_empty()):
            raise IndexError('index out of range')
        else:
            node = self.__start
            count = 0
            while count < key:
                node = node.get_next()
                count += 1
            return node
    
    def __setitem__(self, index, value):
        '''
        Update the node value
        '''
        node = self.__getitem__(index)
        node.set_value(value)

    def __str__(self):
        '''
        Return the string representation.
        '''
        if self.is_empty():
            return '[]'
        else:
            output = '['

            for node in self:
                if node.get_next() is None:
                    output += str(node) + ']'
                else:
                    output += str(node) + ', '
            return output
    
    def __repr__(self):
        return ('Stack(%s)' % self.__str__())