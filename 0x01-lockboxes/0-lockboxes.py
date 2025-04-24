#!/usr/bin/python3
'''canUnlockAll method'''


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened'''
    opened = set()
    start = [0]
    while start:
        num = start.pop()
        if num  not in opened:
            opened.add(num)
            for key in boxes[num]:
                if key < len(boxes) and key not in opened:
                    start.append(key)
    return len(opened) == len(boxes)
