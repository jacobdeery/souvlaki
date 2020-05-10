from lark import Lark, tree


grammar = """
    spec: (NOUN | ADJ) (DELIMITER (NOUN | ADJ))*

    DELIMITER: "-" | " " | "_" | "." | "+" | "/" | ":" | "&"
    NOUN: "noun" | "Noun" | "$Noun" | "NOUN"
    ADJ: "adj" | "Adj" | "$Adj" | "ADJ" | "adjective" | "Adjective" | "$Adjective" | "ADJECTIVE"
"""

parser = Lark(grammar, start='spec')


def parse(string):
    tree = parser.parse(string)
    return [(a.type, str(a)) for a in tree.children]
