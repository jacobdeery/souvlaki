import pytest

import souvlaki as sv


def test_empty_fails():
    string = ''

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_nonsense_fails():
    string = 'nonsense'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_single_noun():
    string = 'noun'

    parsed = sv.parse(string)
    expected = [('NOUN', 'noun')]

    assert parsed == expected


def test_single_adjective():
    string = 'adj'

    parsed = sv.parse(string)
    expected = [('ADJ', 'adj')]

    assert parsed == expected


def test_adjective_and_noun():
    string = 'adj_noun'

    parsed = sv.parse(string)
    expected = [('ADJ', 'adj'), ('DELIMITER', '_'), ('NOUN', 'noun')]

    assert parsed == expected


def test_mixed_delimiters():
    string = 'adj adj_noun'

    parsed = sv.parse(string)
    expected = [('ADJ', 'adj'), ('DELIMITER', ' '), ('ADJ', 'adj'), ('DELIMITER', '_'),
                ('NOUN', 'noun')]

    assert parsed == expected


def test_no_delimiter_fails():
    string = 'nounadj'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_invalid_delimiter_fails():
    string = 'noun^adj'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_parse_single_digit_integer():
    string = '1 adj adj noun'

    parsed = sv.parse(string)
    expected = [('INTEGER', '1'), ('SPACE', ' '), ('ADJ', 'adj'), ('DELIMITER', ' '),
                ('ADJ', 'adj'), ('DELIMITER', ' '), ('NOUN', 'noun')]

    assert parsed == expected


def test_parse_multiple_digit_integer():
    string = '100 adj adj noun'

    parsed = sv.parse(string)
    expected = [('INTEGER', '100'), ('SPACE', ' '), ('ADJ', 'adj'), ('DELIMITER', ' '),
                ('ADJ', 'adj'), ('DELIMITER', ' '), ('NOUN', 'noun')]

    assert parsed == expected


def test_parse_negative_integer_fails():
    string = '-100 adj adj noun'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_parse_float_fails():
    string = '10.0 adj adj noun'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_parse_more_than_one_integer_fails():
    string = '10 10 adj adj noun'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_only_integer_fails():
    string = '10'

    with pytest.raises(Exception):
        parsed = sv.parse(string)
