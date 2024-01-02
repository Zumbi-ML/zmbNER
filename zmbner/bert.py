# -*- coding: UTF-8 -*-

from zmbner.pt_extractors import NerExtractor
import re
from zmbner.utils import normalize
from zmbner.zmb_labels import ZmbLabels
from tqdm import tqdm

def preprocess(text):
    """
    Prepare the text for NER
    """
    text = re.sub(r"\"", "", text)
    text = re.sub(r"\'", "", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r" +", " ", text)
    text = re.sub(r"/", " ", text)

    return text

def to_list(entities_map):
    """
    Convert the sets to lists
    """
    new_map = {}
    for key in entities_map.keys():
        new_map[key] = list(entities_map[key])
    return new_map

class ZmbNER:

    def extract_ents(sentence):
        """
        Returns the entities of a sentence
        """
        entities_map = {}
        ner_extractor = NerExtractor()
        entities_lst = ner_extractor.extract_entities(sentence)
        for entity_tuple in entities_lst:
            entity, label = entity_tuple
            normalized_entity = normalize(entity)
            class_ = ZmbLabels.find_entity_class(label, normalized_entity)
            if (class_ and class_.is_valid(normalized_entity)):
                label = class_.api()
                if (not label in entities_map.keys()):
                    entities_map[label] = set()
                entities_map[label].add(entity)

        return entities_map

    def ents(text, sep='\n'):
        """
        Returns the entities of an article's text
        Args:
            text: the text of the article
            sep: the sentence separator. Defaults to '\n'
        """
        text = preprocess(text)
        entities_map = {}
        
        for sentence in tqdm(text.split(sep)):
            sent_ents_map = ZmbNER.extract_ents(sentence)
            for label in sent_ents_map.keys():
                if (not label in entities_map.keys()):
                    entities_map[label] = sent_ents_map[label]
                entities_map[label].update(sent_ents_map[label])

        return to_list(entities_map)
