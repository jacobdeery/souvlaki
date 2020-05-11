from lark import Lark


grammar = """
    spec: (INTEGER SPACE)? (word) (DELIMITER (word))*
    word: PREFIX* (NOUN | ADJ)

    INTEGER: /[0-9]+/
    SPACE: " "
    DELIMITER: SPACE | "-" | "_" | "." | "+" | "/" | ":" | "&"
    PREFIX: "pre" | "Pre" | "$Pre" | "PRE"
    NOUN: "noun" | "Noun" | "$Noun" | "NOUN"
    ADJ: "adj" | "Adj" | "$Adj" | "ADJ"
"""

parser = Lark(grammar, start='spec')


def tokenize(tree):
    tokens = []
    for child in tree.children:
        try:
            tokens.append((child.type, str(child)))
        except AttributeError:
            tokens += tokenize(child)
    return tokens


def parse(string):
    tree = parser.parse(string)
    return tokenize(tree)
