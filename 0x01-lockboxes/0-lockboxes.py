#!/usr/bin/python3
"""This module has a function that determine if all
    given boxes can be opened
"""


def canUnlockAll(boxes):
    """calculate if all the boxes can be opened given n
        number of locked boxes in front of you.

        Args:
            boxes: a list of lists

        Return:
            return True if all boxes can be opened otherwise
            return False.
    """
    keys = set()
    i = 0
    while i < len(boxes):
        for key in boxes[i]:
            if key >= 1 and key <= len(boxes) - 1 and i != key:
                keys.add(key)
        i += 1
    if sorted(keys) == list(set(range(1, len(boxes)))):
        return True
    else:
        return False
