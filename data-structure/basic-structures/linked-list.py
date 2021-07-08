"""
Federal University of Pernambuco - UFPE
Informatics Center - CIn
Bachelor of Information Systems 
IF969 - Algorithms and Data Structeres
Professor: Hansenclever Bassani
Author: Pedro Manoel Farias Sena de Lima
Email: pmfsl@cin.ufpe.br

Copyright © 2021 all rights reserved

Description: Implementation of Queue data structure.
"""
from node import Node, DoubleLinkedNode

class LinkedList:
    '''
    Linked list implementation
    '''
    def __init__(self):
        self.__start = None
        self.__end = None
    
    def is_empty(self):
        '''
        Return True if stack is empty
        '''
        return self.__start is None
    
    def search(self, value):
        '''
        Return True if a node it is in the list.
        '''
        if self.is_empty():
            return False
        else:
            node = self.__start
            node_found = False
            while node and not(node_found):
                if node.get_value() == value:
                    node_found = True
                else:
                    node = node.get_next()
            return node_found
        
    def insert(self, value):
        '''
        Insert a node in the list
        '''
        node = Node(value)
        if self.is_empty():
            self.__start = self.__end = node
        else:
           self.__end.set_next(node)
           self.__end = node
    
    def remove(self, value):
        '''
        Remove a node from the list
        '''
        if not(self.search(value)):
            raise ValueError('LinkedList.remove(x): x is not in the list')
        else:
            node = self.__start
            previous_node = None
            node_found = False

            while not(node_found):
                if node.get_value() == value:
                    node_found = True
                else:
                    previous_node = node
                    node = node.get_next()
            
            if previous_node is None:
                next_node = node.get_next()
                self.__start.set_next(None)
                self.__start = next_node
            elif node.get_next() is None:
                previous_node.set_next(None)
                self.__end = previous_node
            else:
                previous_node.set_next(node.get_next())
                
    def __len__(self):
        '''
        Return the list length
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
        List iterator
        '''
        self.__index = int()
        return self
    
    def __next__(self):
        '''
        Return the node iterator
        '''
        if self.__index < self.__len__():
            node = self.__getitem__(self.__index)
            self.__index += 1
            return node
        else:
            raise StopIteration
        
    def __getitem__(self, key):
        '''
        Return the node value of the key
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
        Update node value
        '''
        node = self.__getitem__(index)
        node.setValor(value)

    def __str__(self):
        '''
        Return the string representation
        '''
        if self.is_empty():
            return '[]'
        else:
            output = '['

            for node in self:
                if node == self.__end:
                    output += str(node) + ']'
                else:
                    output += str(node) + ', '
            return output

    def __repr__(self):
        return ('LinkedList(%s)' % self.__str__())

class DoubleLinkedList(LinkedList):
    '''
    Double Linked list implementation
    '''
    def insert(self, value):
        '''
        Insere um item na lista
        '''
        node = DoubleLinkedNode(value)
        if self.is_empty():
            print('empty')
            self._LinkedList__start = self._LinkedList__end = node
        else:
            print('not empty')
            self._LinkedList__end.set_next(node)
            node.set_previous(self._LinkedList__end)
            self._LinkedList__end = node
    
    def remove(self, value):
        if not(self.search(value)):
            raise ValueError('DoubleLinkedList.remove(x): x is not in the list')
        else:
            node = self._LinkedList__start
            node_found = False

            while not(node_found):
                if node.get_value() == value:
                    node_found = True
                else:
                    node = node.get_next()
            
            previous_node = node.get_previous()
            next_node = node.get_next()
            if node == self._LinkedList__start:
                node.set_next(None)
                next_node.set_previous(None)
                self._LinkedList__start = next_node
            elif node == self._LinkedList__end:
                node.set_previous(None)
                previous_node.set_next(None)
                self._LinkedList__end = previous_node
            else:
                node.set_next(None)
                node.set_previous(None)
                next_node.set_previous(previous_node)
                previous_node.set_next(next_node)

    def __repr__(self):
        return ('DoubleLinkedList(%s)' % self.__str__())