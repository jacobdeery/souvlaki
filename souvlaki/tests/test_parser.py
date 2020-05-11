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
    lower = 'noun'
    title = 'Noun'
    soft_title = '$Noun'
    upper = 'NOUN'

    parsed_lower = sv.parse(lower)
    parsed_title = sv.parse(title)
    parsed_soft_title = sv.parse(soft_title)
    parsed_upper = sv.parse(upper)

    assert parsed_lower == [('NOUN', 'noun')]
    assert parsed_title == [('NOUN', 'Noun')]
    assert parsed_soft_title == [('NOUN', '$Noun')]
    assert parsed_upper == [('NOUN', 'NOUN')]


def test_single_adj():
    lower = 'adj'
    title = 'Adj'
    soft_title = '$Adj'
    upper = 'ADJ'

    parsed_lower = sv.parse(lower)
    parsed_title = sv.parse(title)
    parsed_soft_title = sv.parse(soft_title)
    parsed_upper = sv.parse(upper)

    assert parsed_lower == [('ADJ', 'adj')]
    assert parsed_title == [('ADJ', 'Adj')]
    assert parsed_soft_title == [('ADJ', '$Adj')]
    assert parsed_upper == [('ADJ', 'ADJ')]


def test_adj_and_noun():
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


def test_integer_only_fails():
    string = '10'

    with pytest.raises(Exception):
        parsed = sv.parse(string)


def test_prefix_on_noun():
    string = 'prenoun'

    parsed = sv.parse(string)
    assert parsed == [('PREFIX', 'pre'), ('NOUN', 'noun')]


def test_prefix_on_adj():
    string = 'preadj'

    parsed = sv.parse(string)
    assert parsed == [('PREFIX', 'pre'), ('ADJ', 'adj')]


def test_multiple_prefixes():
    string = 'preprenoun'

    parsed = sv.parse(string)
    assert parsed == [('PREFIX', 'pre'), ('PREFIX', 'pre'), ('NOUN', 'noun')]


def test_prefix_only_fails():
    string = 'pre'

    with pytest.raises(Exception):
        parsed = sv.parse(string)
