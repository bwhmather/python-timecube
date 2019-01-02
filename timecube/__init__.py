import re
import random

from timecube import _data


_BEGIN = object()
_TERMINATORS = {'.', '!', '?'}


_word_graph = None


def _build_word_graph():
    global _word_graph

    _word_graph = {}

    # Sentences are divided by whitespace preceded by a terminator.  We use a
    # non consuming lookbehind check for the terminator so that it is kept as
    # part of the sentence.
    for sentence in re.split(r'(?<=[\.!?])\s', _data.input_sentences):
        # Split sentence into a list containing a `_BEGIN` token, followed by a
        # list of words, followed by the terminator.
        tokens = [_BEGIN] + sentence[:-1].split() + [sentence[-1]]

        for this, next in zip(tokens[:-1], tokens[1:]):
            successors = _word_graph.setdefault(this, [])
            successors.append(next)


def _get_word_graph():
    if _word_graph is None:
        _build_word_graph()
    return _word_graph


def sentence():
    word_graph = _get_word_graph()

    words = []
    word = random.choice(word_graph[_BEGIN])
    while word not in _TERMINATORS:
        words.append(word)
        word = random.choice(word_graph[word])

    return ' '.join(words) + word
