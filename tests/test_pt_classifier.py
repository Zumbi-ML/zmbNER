import pytest
from zmbner.pt_extractors import NerExtractor

@pytest.fixture
def ner_extractor():
    return NerExtractor()

def test_empty_lst(ner_extractor):
    assert ner_extractor._transform_entities([]) == []

def test_correct_groupping(ner_extractor):
    sentence = \
    """
    Em Goi\u00e2nia, o Brusque venceu o Vila Nova por 3 a 0, mas a partida ficou marcada pelo fato de o clube catarinense acusar um dirigente da equipe goiana de ter chamado o atacante Jefferson Renan de macaco. De Gerson a Luiz Eduardo: entenda o racismo estrutural por tr\u00e1s de epis\u00f3dios recentes no futebol
    """
    expected = \
    [('Goiânia', 'LOCAL'), ('Brusque', 'ORGANIZACAO'), ('Vila Nova', 'ORGANIZACAO'), ('Jefferson Renan', 'PESSOA'), ('Gerson', 'PESSOA'), ('Luiz Eduardo', 'PESSOA')]

    assert expected == ner_extractor.extract_entities(sentence)

def test_only_o_labels(ner_extractor):
    sentence = \
    """
    Esta é uma sentença que não deveria ter uma entidade detectada.
    """
    expected = []
    assert expected == ner_extractor.extract_entities(sentence)

def test_multiple_entities(ner_extractor):
    sentence = \
    """
    Recentemente, foram encontradas evidências adicionais dessa história. Em 1981, arqueólogos escavavam um local chamado Paul Street, no centro da cidade de Exeter, no sul da Inglaterra, e encontraram ossos de peru. Na época, o achado não foi considerado muito significativo. Mas, em 2018, uma nova análise revelou algo surpreendente.
    """
    expected = [('1981', 'TEMPO'), ('Paul Street', 'LOCAL'), ('sul da Inglaterra', 'LOCAL'), ('2018', 'TEMPO')]
    assert expected == ner_extractor.extract_entities(sentence)