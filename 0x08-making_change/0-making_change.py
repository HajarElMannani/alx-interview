#!/usr/bin/python3
"""Function makeChange"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total"""
    if total <= 0:
        return 0
    tbl = [0] + [total + 1] * total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                prec = tbl[i - coin]
                if prec + 1 < tbl[i]:
                    tbl[i] = prec + 1
    if tbl[total] != total + 1:
        return tbl[total]
    else:
        return -1
