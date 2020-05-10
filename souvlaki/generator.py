import souvlaki as sv


def mutate_word(word, style):
    if style.startswith('$'):
        if len(word) < 2:
            return word.upper()
        return word[0].title() + word[1:]
    elif style.islower():
        return word.lower()
    elif style.istitle():
        return word.title()
    elif style.isupper():
        return word.upper()
    else:
        raise ValueError('Could not infer capitalization style from word: ' + str(style))


def generate_word(token, word_source):
    if token[0] == 'NOUN':
        return(mutate_word(word_source.noun(), token[1]))
    elif token[0] == 'ADJ':
        return(mutate_word(word_source.adjective(), token[1]))
    else:
        raise ValueError('Invalid part of speech: ' + str(token[0]))


def generate_from_tokens(tokens, word_source):
    if len(tokens) == 0:
        return ''

    num_names = 1

    if tokens[0][0] == 'INTEGER':
        if len(tokens) < 2:
            raise ValueError('Integer token must be followed by a space')
        num_names = int(tokens[0][1])
        tokens = tokens[2:]
    
    if num_names == 0:
        raise ValueError('Number of names to generate must be nonzero')

    names = []
    for i in range(num_names):
        name = ''
        for token in tokens:
            if token[0] == 'DELIMITER':
                if not token[1] == '&':
                    name += token[1]
            else:
                name += generate_word(token, word_source)
        names.append(name)

    if num_names == 1:
        return names[0]

    return names


def generate(string, word_source):
    return generate_from_tokens(sv.parse(string), word_source)
