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


def generate_name(tokens, word_source):
    name = ''
    for token in tokens:
        if token[0] == 'DELIMITER':
            if not token[1] == '&':
                name += token[1]
        else:
            name += generate_word(token, word_source)

    return name
