#!/usr/bin/python3
"""
0-lockboxes.py

This module contains the canUnlockAll function that determines
if all boxes in a list of lists can be unlocked.

Author: Your Name
Date: Date of completion
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists, where each list represents a box
                      and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set()
    opened.add(0)
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened and key < n:
                opened.add(key)
                stack.append(key)

    return len(opened) == n
