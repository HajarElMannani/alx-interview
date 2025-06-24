#!/usr/bin/python3
"""Function isWinner"""


def isWinner(x, nums):
    """Function that returns the  name of the player
    that won the most rounds"""
    if x < 1 or not nums:
        return None
    num = max(nums)
    prime = [False, False] + [True] * (num - 1)
    for i in range(2, int(num ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, num + 1, i):
                prime[j] = False
    count_primes = [0] * (num + 1)
    cnt = 0
    for i in range(len(count_primes)):
        if prime[i] is not None:
            cnt += 1
        count_primes[i] = cnt
    maria_win = 0
    ben_win = 0
    for number in nums:
        if count_primes[number] % 2 == 1:
            maria_win += 1
        else:
            ben_win += 1
    if maria_win < ben_win:
        return "Ben"
    elif ben_win < maria_win:
        return "Maria"
    else:
        return None
    
