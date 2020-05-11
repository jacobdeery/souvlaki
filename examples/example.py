import os
import random

import souvlaki as sv


class WordSource():
    def __init__(self, nouns, adjectives, prefixes):
        self.nouns = nouns
        self.adjectives = adjectives
        self.prefixes = prefixes
    
    def noun(self):
        return random.choice(self.nouns)

    def adjective(self):
        return random.choice(self.adjectives)

    def prefix(self):
        return random.choice(self.prefixes)


def main():
    here = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(here, 'rocket_nouns.txt')) as noun_file:
        nouns = noun_file.read().splitlines()

    with open(os.path.join(here, 'rocket_adjectives.txt')) as adj_file:
        adjectives = adj_file.read().splitlines()

    with open(os.path.join(here, 'rocket_prefixes.txt')) as pre_file:
        prefixes = pre_file.read().splitlines()

    source = WordSource(nouns, adjectives, prefixes)

    spec = '10 $Adj $Adj $Preadj $Noun'
    names = sv.generate(spec, source)

    for name in names:
        print(name)


if __name__ == "__main__":
    main()
