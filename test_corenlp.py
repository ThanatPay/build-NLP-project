from nlplogic.corenlp import get_phrases

def test_get_phrase():
    assert 'bangkok' in get_phrases('Bangkok')