import pytest

import souvlaki as sv


class SimpleWordSource:
    def noun(self):
        return 'knight'
    def adjective(self):
        return 'tricky'


def test_mutate_word_invalid():
    word = 'choreography'

    with pytest.raises(ValueError):
        sv.mutate_word(word, 'cHoReOgRaPhY')


def test_mutate_noun():
    noun = 'Portugal'

    assert sv.mutate_word(noun, 'noun') == 'portugal'
    assert sv.mutate_word(noun, 'Noun') == 'Portugal'
    assert sv.mutate_word(noun, 'NOUN') == 'PORTUGAL'


def test_mutate_adjective():
    adjective = 'incredulous'

    assert sv.mutate_word(adjective, 'adj') == 'incredulous'
    assert sv.mutate_word(adjective, 'adjective') == 'incredulous'
    assert sv.mutate_word(adjective, 'Adj') == 'Incredulous'
    assert sv.mutate_word(adjective, 'Adjective') == 'Incredulous'
    assert sv.mutate_word(adjective, 'ADJ') == 'INCREDULOUS'
    assert sv.mutate_word(adjective, 'ADJECTIVE') == 'INCREDULOUS'


def test_mutate_word_titlecase():
    allcaps_noun = 'ATM'
    allcaps_adj = 'FURIOUS'

    assert sv.mutate_word(allcaps_noun, 'Noun') == 'Atm'
    assert sv.mutate_word(allcaps_noun, '$Noun') == 'ATM'
    assert sv.mutate_word(allcaps_adj, 'Adj') == 'Furious'
    assert sv.mutate_word(allcaps_adj, '$Adj') == 'FURIOUS'
    assert sv.mutate_word(allcaps_adj, 'Adjective') == 'Furious'
    assert sv.mutate_word(allcaps_adj, '$Adjective') == 'FURIOUS'


def test_generate_word_noun():
    source = SimpleWordSource()

    lower = sv.generate_word(('NOUN', 'noun'), source)
    title = sv.generate_word(('NOUN', 'Noun'), source)
    upper = sv.generate_word(('NOUN', 'NOUN'), source)

    assert lower == 'knight'
    assert title == 'Knight'
    assert upper == 'KNIGHT'


def test_generate_word_adjective():
    source = SimpleWordSource()

    lower = sv.generate_word(('ADJ', 'adj'), source)
    title = sv.generate_word(('ADJ', 'Adj'), source)
    upper = sv.generate_word(('ADJ', 'ADJ'), source)

    assert lower == 'tricky'
    assert title == 'Tricky'
    assert upper == 'TRICKY'


def test_generate_name_empty():
    tokens = []

    assert sv.generate_name(tokens, None) == ''


def test_generate_name_simple():
    tokens = [('ADJ', 'adj'), ('DELIMITER', ' '), ('NOUN', 'noun')]

    assert sv.generate_name(tokens, SimpleWordSource()) == 'tricky knight'


def test_generate_name_complex():
    tokens = [('ADJ', 'adj'), ('DELIMITER', '_'), ('ADJ', 'Adjective'), ('DELIMITER', '&'),
              ('NOUN', 'NOUN')]

    assert sv.generate_name(tokens, SimpleWordSource()) == 'tricky_TrickyKNIGHT'
