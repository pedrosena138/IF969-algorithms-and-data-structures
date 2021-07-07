"""
Federal University of Pernambuco - UFPE
Informatics Center - CIn
Bachelor of Information Systems IF969 - Algorithms and Data Structeres
Professor: Hansenclever Bassani
Author: Pedro Manoel Farias Sena de Lima
Email: pmfsl@cin.ufpe.br

Copyright © 2021 all rights reserved

Description: Implementation of node structure.
"""

class Node:
    '''
    Queue node
    '''
    def __init__(self, value=None):
        self.__value = value
        self.__next = None
    
    #Value Get and Set
    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value

    #Next Get and Set
    def get_next(self):
        return self.__next
    def set_next(self, node):
        self.__next = node
    
    def __str__(self):
        return str(self.__value)
    
    def __repr__(self):
        return self.__value