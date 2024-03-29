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
from node import Node

class Queue:
    '''
    Queue implementation
    '''
    def __init__(self):
        self.__start = None
        self.__end = None
    
    def is_empty(self):
        '''
        Return True if queue is empty
        '''
        return self.__start is None
    
    def search(self, value):
        '''
        Return True if a node it is in the queue.
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
        
    def enqueue(self, value):
        '''
        Insert a value in the queue
        '''
        node = Node(value)
        if self.is_empty():
            self.__start = self.__end = node
        else:
           self.__end.set_next(node)
           self.__end = node

    def dequeue(self):
        '''
        Remove the first value from the queue.
        '''
        if self.is_empty():
            raise ValueError('Queue.dequeue(): empty queue')
        else:
            next_node = self.__start.get_next()
            self.__start.set_next(None)
            self.__start = next_node
    
    def __len__(self):
        '''
        Return queue length
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
        Queue iterator
        '''
        self.__index = int()
        return self
    
    def __next__(self):
        '''
        Return node iterator
        '''
        if self.__index < self.__len__():
            node = self.__getitem__(self.__index)
            self.__index += 1
            return node
        else:
            raise StopIteration
        
    def __getitem__(self, key):
        '''
        Retorna o valor do no que contem a chave passada como parametro
        '''
        index = self.__len__() - 1
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
        node.set_value(value)

    def __str__(self):
        '''
        Return string representation
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
        return ('Queue(%s)' % self.__str__())
