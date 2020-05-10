from lark import Lark


grammar = """
    spec: (INTEGER SPACE)? (NOUN | ADJ) (DELIMITER (NOUN | ADJ))*

    INTEGER: /[0-9]+/
    SPACE: " "
    DELIMITER: SPACE | "-" | "_" | "." | "+" | "/" | ":" | "&"
    NOUN: "noun" | "Noun" | "$Noun" | "NOUN"
    ADJ: "adj" | "Adj" | "$Adj" | "ADJ" | "adjective" | "Adjective" | "$Adjective" | "ADJECTIVE"
"""

parser = Lark(grammar, start='spec')


def parse(string):
    tree = parser.parse(string)
    return [(a.type, str(a)) for a in tree.children]
