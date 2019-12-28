#!/usr/bin/env bash

"""
cells module: has class Cell with functions add_data, search_list, get_list_length,
            save_data_to_file, restore_data_from_file, cleanup.
"""
import pickle
import os


cells_list = [] #list of Cell objects

class Cell:
    
    def __init__(self, ID, header, content):
        self.ID = ID
        self.header = header
        self.content = content

    def add_data(self):
        cells_list.append(self)

    @staticmethod
    def search_list(dictionary): # TEST
        for c in cells_list:
            if c == dictionary:
                print("found dictionary search!\n", type(c), c)
                return c
                
    @staticmethod
    def get_list_length():
        return len(cells_list)

    @staticmethod
    def save_data_to_file(filename):
        with open(filename, 'wb') as file_object:
            serialized = cells_list
            pickle.dump(serialized, file_object)
            file_object.close()
            
        cells_list.clear()
        
    @staticmethod
    def restore_data_from_file(filename):
        with open(filename, 'rb') as file_object:
            raw_data = file_object.read()
            
        deserialized = pickle.loads(raw_data)
        file_object.close()
        cells_list = deserialized 

    def cleanup(self):
        pass
        
    def __str__(self): #TEST
        return(str(vars(self)))
        #return "{ID: {0}, header: {1}, content: {2}}".format(self.ID, self.header, self.content)


