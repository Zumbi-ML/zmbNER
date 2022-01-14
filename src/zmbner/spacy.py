# -*- coding: UTF-8 -*-

import pt_zmbner
from zmbner.zmb_labels import ZmbLabels
import re
from zmbner.utils import normalize

nlp = pt_zmbner.load()

def preprocess(text):
    """
    Prepare the text for NER
    """
    text = re.sub(r"\"", "", text)
    text = re.sub(r"\'", "", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r" +", " ", text)
    return text

class ZmbNER:

    def extract_ents_from_a_sentence(sentence):
        """
        Returns the entities of a sentence
        """
        entities_map = {}

        doc = nlp(sentence)
        for entity in doc.ents:
            normalized_entity = normalize(entity.text)
            class_ = ZmbLabels.find_entity_class(entity.label_, normalized_entity)
            if (class_.is_valid(normalized_entity)):
                label = class_.api()
                if (not label in entities_map.keys()):
                    entities_map[label] = set()
                entities_map[label].add(entity.text)

        return entities_map

    def extract_ents_from_an_article(text, sep='\n'):
        """
        Returns the entities of an article's text
        Args:
            text: the text of the article
            sep: the sentence separator. Defaults to '\n'
        """
        text = preprocess(text)
        entities_map = {}

        for sentence in text.split(sep):
            sent_ents_map = ZmbNER.extract_ents_from_a_sentence(sentence)
            for label in sent_ents_map.keys():
                if (not label in entities_map.keys()):
                    entities_map[label] = sent_ents_map[label]
                entities_map[label].update(sent_ents_map[label])

        return entities_map
