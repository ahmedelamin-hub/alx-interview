#!/usr/bin/python3
"""Game of prime number elimination between two players."""


def isWinner(x, nums):
    """
    Determines who wins more rounds in a prime game between Maria and Ben.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list where each value represents the upper limit

    Returns:
        str: Name of the player with more wins ("Maria" or "Ben").
        None: If there is no clear winner.
    """
    # Validate inputs
    if not nums or x <= 0 or x != len(nums):
        return None

    # Initialize player scores
    ben_wins = 0
    maria_wins = 0

    # Generate a list to mark primes up to the maximum value in nums
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    # Generate primes using the Sieve of Eratosthenes method
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Evaluate each round based on the prime count
    for n in nums:
        prime_count = sum(primes[2:n + 1])  # Count primes up to n
        if prime_count % 2 == 0:
            ben_wins += 1  # Ben wins if the count is even
        else:
            maria_wins += 1  # Maria wins if the count is odd

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


def rm_multiples(ls, prime):
    """
    Marks non-prime multiples of a given number in the list.

    Args:
        ls (list): List representing whether numbers are prime.
        prime (int): The prime number whose multiple

    Returns:
        None
    """
    # Starting from 2, eliminate all multiples of the given prime
    for i in range(2, len(ls)):
        multiple = i * prime
        if multiple >= len(ls):
            break
        ls[multiple] = False
