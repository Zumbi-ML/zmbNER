# -*- coding: UTF-8 -*-

from zmbner import config

def read_file(filename, sep='\n'):
    """
    Read and split a file
    """
    with open(filename, 'r') as f:
        return f.read().split(sep)

def get_filename(entity_name):
    """
    Make a filename out of an entity name
    """
    return config.RESOURCES_DIR + entity_name + ".tsv"
