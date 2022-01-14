# -*- coding: UTF-8 -*-

from zmbner import config
import re

def read_file(filename, sep='\n'):
    """
    Read and split a file
    """
    known_entities = []
    with open(filename, 'r') as f:
         known_entities = f.read().split(sep)

    for i in range(len(known_entities)):
        known_entities[i] = normalize(known_entities[i])
    return known_entities

def get_filename(entity_name):
    """
    Make a filename out of an entity name
    """
    return config.RESOURCES_DIR + entity_name + ".tsv"

def normalize(an_entity):
    """
    Normalize an entity name for appropriate recognition
    Args:
        an_entity: E.g., Procuradoria-Geral da República
    Returns:
        The normalized entity. E.g., procuradoria geral da republica
    """
    an_entity = an_entity.lower()
    an_entity = re.sub(r"-", " ", an_entity)
    an_entity = re.sub(r"\.", " ", an_entity)
    an_entity = re.sub(r",", " ", an_entity)
    an_entity = re.sub(r"á", "a", an_entity)
    an_entity = re.sub(r"à", "a", an_entity)
    an_entity = re.sub(r"ã", "a", an_entity)
    an_entity = re.sub(r"é", "e", an_entity)
    an_entity = re.sub(r"è", "e", an_entity)
    an_entity = re.sub(r"ê", "e", an_entity)
    an_entity = re.sub(r"í", "i", an_entity)
    an_entity = re.sub(r"õ", "o", an_entity)
    an_entity = re.sub(r"ó", "o", an_entity)
    an_entity = re.sub(r"ò", "o", an_entity)
    an_entity = re.sub(r"ú", "u", an_entity)
    an_entity = re.sub(r"ù", "u", an_entity)
    an_entity = re.sub(r"ç", "c", an_entity)
    an_entity = re.sub(r" +", " ", an_entity)
    return an_entity
