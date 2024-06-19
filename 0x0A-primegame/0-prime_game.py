#!/usr/bin/python3
"""Prime Game"""


def is_prime(n):
    """Check if n is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_primes(n, primes):
    """Calculate primes"""
    for i in range(n + 1):
        if is_prime(i):
            primes.append(i)


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or not nums:
        return None
    primes = []
    calculate_primes(max(nums), primes)
    wins = 0
    for n in nums:
        if n in primes:
            wins += 1
    if wins % 2 == 0:
        return "Maria"
    return "Ben"
