#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    def sieve(n):
        """ Sieve of Eratosthenes to find all primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_nums = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_nums

    def play_game(n, primes):
        """ Simulate a single game with given n and list of primes """
        primes_set = set(primes)
        current_set = set(range(1, n + 1))
        turn = 0  # Maria's turn if even, Ben's turn if odd

        while primes_set:
            # Find the smallest prime in the current set
            prime = next((p for p in primes_set if p in current_set), None)
            if prime is None:
                break  # No more primes to pick, current player loses
            multiples = set(range(prime, n + 1, prime))
            current_set -= multiples
            turn += 1  # Switch turn

            # Remove picked prime and its multiples from prime set
            primes_set -= multiples

        # If turn is even, it means Ben cannot play, so Maria wins
        # If turn is odd, it means Maria cannot play, so Ben wins
        return "Maria" if turn % 2 == 1 else "Ben"

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
