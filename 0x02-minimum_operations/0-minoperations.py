#!/usr/bin/python3
'''Function minOperations'''


def minOperations(n):
    '''method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file'''
    operation = 0
    fact = 2
    if n < 2:
        return 0
    while n > 1:
        while n % fact == 0:
            operation += fact
            n //= fact
        fact += 1
    return operation
