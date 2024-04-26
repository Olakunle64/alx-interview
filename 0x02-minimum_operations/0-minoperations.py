#!/usr/bin/python3
"""This module has a function named <minOperations>"""


def checkPrime(n, p):
    """This function checks if a number is prime or not

        Args:
            n: an integer
            p: an integer

        Return: True if n is prime otherwise False
    """
    if p > n:
        return False
    if n % p > 0 or n == p:
        return True
    else:
        return False
    return checkPrime(n, p + 1)


def minOperations(n):
    """This function calculates the minimum operations needed
        result in exactly n H characters in the file

        Args:
            n: an integer

        Return: return the minimum operations needed as an integer
    """
    if (n <= 1):
        return 0
    total_prime_factors = 0
    prime = 2
    tempPrime = 2
    while n > 1:
        if n % prime == 0:
            tempPrime = prime
            total_prime_factors += prime
            n = n / prime
        else:
            tempPrime += 1
            if checkPrime(tempPrime, 2):
                prime = tempPrime
    return total_prime_factors
