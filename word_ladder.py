#!/bin/python3

from copy import deepcopy
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):

    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    dictionary = open(dictionary_file)
    words = dictionary.read().split('\n')
    # create a stack
    # this intializes a stack!
    list = []
    # push first word into stack
    list.append(start_word)
    # create a queue
    queue = deque()
    queue.append(list)

    if start_word == end_word:
        return list
    # while the queue is not empty, dequeue a stack from the queue
    while len(queue) != 0:
        topstack = queue.pop()
        copy = deepcopy(words)

        for word in set(copy):
            if _adjacent(word, topstack[-1]) is True:
                stack_copied = deepcopy(topstack)
                stack_copied.append(word)

                if word == end_word:
                    return stack_copied

                queue.appendleft(stack_copied)
                words.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    i = 0

    if len(ladder) == 0:
        return False
    while i < len(ladder) - 1:
        if _adjacent(ladder[i], ladder[i + 1]) is True:
            i += 1
        else:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    i = 0
    if word1 == word2:
        return False

    if len(word1) == len(word2):
        for a, b in zip(word1, word2):
            if a != b:
                i += 1

    if i == 1:
        return True
    else:
        return False
