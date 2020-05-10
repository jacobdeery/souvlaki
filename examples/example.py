import os
import random

import souvlaki as sv


class WordSource():
    def __init__(self, nouns, adjectives):
        self.nouns = nouns
        self.adjectives = adjectives
    
    def noun(self):
        return random.choice(self.nouns)

    def adjective(self):
        return random.choice(self.adjectives)


def main():
    here = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(here, 'rocket_nouns.txt')) as noun_file:
        nouns = noun_file.read().splitlines()

    with open(os.path.join(here, 'rocket_adjectives.txt')) as adj_file:
        adjectives = adj_file.read().splitlines()

    source = WordSource(nouns, adjectives)

    spec = '$Adj $Adj $Adj $Noun'

    for i in range(20):
        print(sv.generate(spec, source))


if __name__ == "__main__":
    main()
