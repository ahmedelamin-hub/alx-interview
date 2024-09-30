#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """function find all primes up to n"""
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def isWinner(x, nums):
    """Determine the winner after x rounds of the prime game"""
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to calculate primes up to that number
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        prime_count = 0
        for prime in primes:
            if prime > n:
                break
            prime_count += 1

        # Maria wins if the prime count is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
