# Souvlaki

Souvlaki is a simple utility for generating memorable names from strings of adjectives and nouns.

## Usage

A souvlaki spec (recipe?) is a string of "adjective" and "noun" tokens separated by delimiters.

An adjective token is one of the following:
- `adj`, `Adj`, `$Adj`, `ADJ`, `adjective`, `Adjective`, `$Adjective`, `ADJECTIVE`

A noun token is one of the following:
- `noun`, `Noun`, `$Noun`, `NOUN`

A delimiter is one of the following:
- `-`, ` ` (space), `_`, `.`, `+`, `/`, `:`, `&`

Souvlaki will replace adjective and noun tokens with adjectives and nouns, respectively. The capitalization style of the token (`lower`, `Title`, `UPPER`) will be copied. If the token uses the `$Title` style, souvlaki will ensure the first letter is capitalized but will not modify the rest of the word - so `taco` becomes `Taco`, but `ICBM` remains `ICBM`.

The special delimiter `&` indicates that words should be directly concatenated (so `adj&adj` might yield `angryred`).

See `examples/example.py` for an example.

## Why "souvlaki"?

Names are often generated in the format `adj-adj-noun` (like `sintered-ductile-diode`), which is typically called "kebab case" since it looks like a kebab. `kebab` was already taken on PyPI, and `souvlaki` was the next best thing.
