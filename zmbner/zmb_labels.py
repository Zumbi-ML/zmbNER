# -*- coding: UTF-8 -*-

from zmbner import config
from zmbner.utils import read_file, get_filename
import re

class ZmbLabels:

    class SOURCE:
        entity_name = "SOURCE"

        def api(an_entity=None):
            return "sources"

        def ner():
            return None

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.SOURCE.is_known(an_entity)

    class LOCAL:
        entity_name = "LOCAL"

        def api(an_entity=None):

            if (an_entity):

                if (ZmbLabels.CITY.is_known(an_entity)):
                    return ZmbLabels.CITY.api()

                elif (ZmbLabels.STATE.is_known(an_entity)):
                    return ZmbLabels.STATE.api()

                elif (ZmbLabels.COUNTRY.is_known(an_entity)):
                    return ZmbLabels.COUNTRY.api()

            return "local"

        def ner():
            return ZmbLabels.LOCAL.entity_name

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.LOCAL.is_known(an_entity)
        
    class MEDIA:
        entity_name = "MEDIA"

        def api(an_entity=None):
            return "media"

        def ner():
            return None

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.MEDIA.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.MEDIA.is_known(an_entity)

    class LAW:
        entity_name = "LEGISLACAO"

        def api(an_entity=None):
            return "laws"

        def ner():
            return None

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.LAW.is_known(an_entity)

    class MOVEMENT:
        entity_name = "MOVEMENT"

        def api(an_entity=None):
            return "movements"

        def ner():
            return ZmbLabels.MOVEMENT.entity_name

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.MOVEMENT.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.MOVEMENT.is_known(an_entity)

    class PEOPLE:
        entity_name = "PESSOA"

        def api(an_entity=None):
            return "people"

        def ner():
            return ZmbLabels.PEOPLE.entity_name

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            known_uses_lst = ZmbLabels.is_known_as(an_entity)

            is_known_as_sth_else = len(known_uses_lst) > 2 or \
                                   (len(known_uses_lst) == 1 and \
                                   known_uses_lst[0] != ZmbLabels.PEOPLE.api())

            if (an_entity.isupper() or is_known_as_sth_else):
                return False

            return True

        def is_handler(an_entity):
            return ZmbLabels.PEOPLE.is_known(an_entity)

    class ORG:
        entity_name = "ORGANIZACAO"

        def api(an_entity=None):

            if (an_entity):

                if (ZmbLabels.PUBLIC.is_known(an_entity)):
                    return ZmbLabels.PUBLIC.api()

                elif (ZmbLabels.EDUCATIONAL.is_known(an_entity)):
                    return ZmbLabels.EDUCATIONAL.api()

                elif (ZmbLabels.MOVEMENT.is_known(an_entity)):
                    return ZmbLabels.MOVEMENT.api()

                elif (ZmbLabels.POLICE.is_known(an_entity)):
                    return ZmbLabels.POLICE.api()

                elif (ZmbLabels.POLITICAL.is_known(an_entity)):
                    return ZmbLabels.POLITICAL.api()

                elif (ZmbLabels.MEDIA.is_known(an_entity)):
                    return ZmbLabels.MEDIA.api()

                return ZmbLabels.ORG.api()

            return None

        def ner():
            return ZmbLabels.ORG.entity_name

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.ORG.is_known(an_entity)

    class PRIVATE:
        entity_name = "PRIVATE"

        def api(an_entity=None):
            return "private"

        def ner():
            return ZmbLabels.ORG.entity_name

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            known_uses_lst = ZmbLabels.is_known_as(an_entity)

            is_known_as_sth_else = len(known_uses_lst) > 2 or \
                                   (len(known_uses_lst) == 1 and \
                                   known_uses_lst[0] != ZmbLabels.PRIVATE.api())

            if (is_known_as_sth_else):
                return False
            return True

        def is_handler(an_entity):
            return ZmbLabels.PRIVATE.is_known(an_entity)

    class PUBLIC:
        entity_name = "PUBLIC"

        def api(an_entity=None):
            return "public"

        def ner():
            return None

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.PUBLIC.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            return ZmbLabels.PUBLIC.is_known(an_entity)

        def is_handler(an_entity):
            return ZmbLabels.PUBLIC.is_known(an_entity)

    class EDUCATIONAL:
        entity_name = "EDUCATIONAL"

        def api(an_entity=None):
            return "educational"

        def ner():
            return None

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.EDUCATIONAL.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            an_entity = an_entity.lower()

            return ZmbLabels.EDUCATIONAL.is_known(an_entity) or \
                    "university" in an_entity or \
                    "universidade" in an_entity or \
                    "colegio" in an_entity or \
                    "college" in an_entity or \
                    "escola" in an_entity or \
                    "faculdade" in an_entity or \
                    "school" in an_entity

        def is_handler(an_entity):
            return ZmbLabels.EDUCATIONAL.is_valid(an_entity)

    class WORK:
        entity_name = "WORK"

        def api(an_entity=None):
            return "works"

        def ner():
            return ZmbLabels.WORK.entity_name

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.WORK.is_known(an_entity)

    class COUNTRY:
        entity_name = "COUNTRY"

        def api(an_entity=None):
            return "countries"

        def ner():
            return ZmbLabels.COUNTRY.entity_name

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.COUNTRY.entity_name)
            known_lst = read_file(filepath)
            result = an_entity.lower() in known_lst
            return result

        def is_valid(an_entity):
            return ZmbLabels.COUNTRY.is_known(an_entity)

        def is_handler(an_entity):
            return ZmbLabels.COUNTRY.is_known(an_entity)

    class STATE:
        entity_name = "STATE"

        def api(an_entity=None):
            return "states"

        def ner():
            return ZmbLabels.STATE.entity_name

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.STATE.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            return ZmbLabels.STATE.is_known(an_entity)

        def is_handler(an_entity):
            return ZmbLabels.STATE.is_known(an_entity)

    class CITY:
        entity_name = "CITY"

        def api(an_entity=None):
            return "cities"

        def ner():
            return ZmbLabels.CITY.entity_name

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.CITY.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            return ZmbLabels.CITY.is_known(an_entity)

        def is_handler(an_entity):
            return ZmbLabels.CITY.is_known(an_entity)

    class POLICE:
        entity_name = "POLICE"

        def api(an_entity=None):
            return "polices"

        def ner():
            return None

        def is_known(an_entity):
            filepath = get_filename(ZmbLabels.POLICE.entity_name)
            known_lst = read_file(filepath)
            return an_entity.lower() in known_lst

        def is_valid(an_entity):
            return ZmbLabels.POLICE.is_known(an_entity)

        def is_handler(an_entity):
            return ZmbLabels.POLICE.is_known(an_entity)

    class ACTION:
        entity_name = "ACTION"

        def api(an_entity=None):
            return "actions"

        def ner():
            return None

        def is_known(an_entity):
            return False

        def is_valid(an_entity):
            return True

        def is_handler(an_entity):
            return ZmbLabels.ACTION.is_known(an_entity)

    class POLITICAL:
        entity_name = "POLITICAL"

        def api(an_entity=None):
            return "political"

        def ner():
            return None

        def is_known(an_entity):
            states = ['al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg', 'ms', 'mt', 'pa', 'pb', 'pe', 'pi', 'pr', 'rj', 'rn', 'ro', 'rr', 'rs', 'sc', 'se', 'sp', 'to']

            filepath = get_filename(ZmbLabels.POLITICAL.entity_name)
            known_lst = read_file(filepath)

            if (an_entity.lower() in known_lst):
                return True

            sep = " " # This separator has to match the one from normalization
            state_political_parties = [party + sep + state for party in known_lst for state in states]

            return an_entity.lower() in state_political_parties

        def is_valid(an_entity):
            return ZmbLabels.POLITICAL.is_known(an_entity)

        def is_handler(an_entity):
            return ZmbLabels.POLITICAL.is_known(an_entity)

    def is_known_as(an_entity):
        """
        Returns a list of known uses for this entity
        """
        known_ent_lst = []
        if (ZmbLabels.PEOPLE.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.PEOPLE.api())

        elif (ZmbLabels.PUBLIC.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.PUBLIC.api())

        elif (ZmbLabels.EDUCATIONAL.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.EDUCATIONAL.api())

        elif (ZmbLabels.MOVEMENT.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.MOVEMENT.api())

        elif (ZmbLabels.POLICE.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.POLICE.api())

        elif (ZmbLabels.POLITICAL.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.POLITICAL.api())

        elif (ZmbLabels.CITY.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.CITY.api())

        elif (ZmbLabels.STATE.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.STATE.api())

        elif (ZmbLabels.COUNTRY.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.COUNTRY.api())

        elif (ZmbLabels.MEDIA.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.MEDIA.api())

        elif (ZmbLabels.WORK.is_known(an_entity)):
            known_ent_lst.append(ZmbLabels.WORK.api())

        return known_ent_lst

    def find_entity_class(ner_clf_label, an_entity):
        """
        Finds the class that can handle the entity.
        Only the entities that are classified by the zmbner_clf are needed in the IFs
        """
        if (ner_clf_label == ZmbLabels.PEOPLE.entity_name):
            return ZmbLabels.PEOPLE

        elif (ner_clf_label == ZmbLabels.ORG.entity_name):
            # This is where its inferred the correct entity class

            if (ZmbLabels.PUBLIC.is_handler(an_entity)):
                return ZmbLabels.PUBLIC

            if (ZmbLabels.EDUCATIONAL.is_handler(an_entity)):
                return ZmbLabels.EDUCATIONAL

            if (ZmbLabels.MOVEMENT.is_handler(an_entity)):
                return ZmbLabels.MOVEMENT

            if (ZmbLabels.POLICE.is_handler(an_entity)):
                return ZmbLabels.POLICE

            if (ZmbLabels.POLITICAL.is_handler(an_entity)):
                return ZmbLabels.POLITICAL

            if (ZmbLabels.MEDIA.is_handler(an_entity)):
                return ZmbLabels.MEDIA

            # If we can't find it, we assume it is an ORG
            return ZmbLabels.ORG

        elif (ner_clf_label == ZmbLabels.LOCAL.entity_name):

            if (ZmbLabels.COUNTRY.is_handler(an_entity)):
                return ZmbLabels.COUNTRY

            if (ZmbLabels.STATE.is_handler(an_entity)):
                return ZmbLabels.STATE

            if (ZmbLabels.CITY.is_handler(an_entity)):
                return ZmbLabels.CITY
            
            # If we can't find it, we assume it is an LOCAL
            return ZmbLabels.LOCAL

        elif (ner_clf_label == ZmbLabels.WORK.entity_name):
            return ZmbLabels.WORK

        return None